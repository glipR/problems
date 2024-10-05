#include <cmath>
#include <iostream>
#include <complex>
#include <algorithm>
#include <vector>

using namespace std;

typedef complex<double> cd;
const double PI = acos(-1);

// FFT and IFFT of a vector a.
// If using for polynomial multiplication, just get the real portion with round(a[i].real()) at the end (doing away with the round if floating points are needed.)
void fft(vector<cd> & a, bool invert=false) {
    int n = a.size(), i, j, len; cd w, u, v;
    for (i=1, j=0;i<n;i++) {
        int bit = n/2; for (;j>=bit; bit /=2) j -= bit;
        j += bit; if (i<j) swap(a[i], a[j]);
    }
    for (len=2;len<=n; len<<=1) {
        double ang = 2*PI/len*(invert?-1:1); cd wlen=polar(1.0, ang);
        for (i=0;i<n;i += len) for (j=0,w=1;j<len/2; j++)
            u=a[i+j], v=a[i+j+len/2]*w, a[i+j]=u+v, a[i+j+len/2]=u-v, w*=wlen;
    }
    if (invert) for(i=0;i<n;i++) a[i]/=n;
}

vector<cd> multiply(vector<cd> const& a, vector<cd> const& b) {
    int i, n; vector<cd> fa(a.begin(), a.end()), fb(b.begin(), b.end());
    for (n=1;n<2*(int)max(a.size(), b.size());n*=2);
    fa.resize(n), fb.resize(n), fft(fa), fft(fb);
    for (i=0;i<n;i++) fa[i]*=fb[i];
    fft(fa, true);
    return fa;
}

#define MAXN 1000000
#define MAXM 1000000

int dna[MAXN];
int match[MAXM];
char subs[MAXM+MAXN+MAXN];
double probs[MAXM];
vector<cd> fftdna;
vector<cd> fftmatch;
vector<cd> blockdna;
vector<cd> blockmatch;
cd c_i = {0, 1};

bool special_comp(pair<pair<bool, double>, int> a, pair<pair<bool, double>, int> b) {
    if (a.first.first != b.first.first) return a.first.first > b.first.first;
    return a.first.second > b.first.second;
}

int main() {

    int n, m, n_requires;
    n_requires = 0;
    cin >> n >> m;

    for (int i=0; i<n; i++) cin >> dna[i];
    for (int i=0; i<m; i++) cin >> match[i];
    for (int i=0; i<m; i++) cin >> probs[i];

    fftdna.assign(2*n, 0);
    fftmatch.assign(m, 0);
    blockdna.assign(2*n, 0);
    blockmatch.assign(m, 0);

    for (int i=0; i<m; i++) {
        int ins_index = m-i-1;
        if ((probs[i] == 0 && match[i] == 0) || (probs[i] == 1 && match[i] == 1)) {
            // Originally a 0, for sure. The z_array will find any inconsistencies.
            fftmatch[ins_index] = {0, 0};
            blockmatch[ins_index] = {1, 0};
            n_requires ++;
        }
        else if ((probs[i] == 0 && match[i] == 1) || (probs[i] == 1 && match[i] == 0)) {
            // Originally a 1, for sure. The z_array will find any inconsistencies.
            fftmatch[ins_index] = {0, 0};
            blockmatch[ins_index] = {0, -1};
            n_requires ++;
        }
        else {
            blockmatch[ins_index] = {0, 0};
            // Some probability between 0.1 and 0.9.
            double lg_flip = log(probs[i]);
            double lg_same = log(1 - probs[i]);
            if (match[i] == 0) {
                fftmatch[ins_index] = {lg_same, lg_flip};
            } else {
                fftmatch[ins_index] = {lg_flip, lg_same};
            }
        }
    }

    for (int i=0; i<n; i++) {
        if (dna[i] == 0) {
            fftdna[i] = {1, 0};
            blockdna[i] = {1, 0};
        }
        else {
            fftdna[i] = {0, -1};
            blockdna[i] = {0, 1};
        }
    }
    for (int i=0; i<n; i++) {
        fftdna[n+i] = fftdna[i];
        blockdna[n+i] = blockdna[i];
    }

    for (int i=0; i<m; i++) {
        if (probs[i] == 0) {
            if (match[i] == 1) subs[i] = '1';
            else subs[i] = '0';
        } else if (probs[i] == 1) {
            if (match[i] == 1) subs[i] = '0';
            else subs[i] = '1';
        } else subs[i] = 'x';
    }

    for (int i=0; i<n; i++) {
        int idx1 = m+i;
        int idx2 = m+n+i;
        char j;
        if (dna[i] == 0) j = '0';
        else j = '1';
        subs[idx1] = j;
        subs[idx2] = j;
    }

    auto res = multiply(fftdna, fftmatch);
    auto res2 = multiply(blockdna, blockmatch);

    // Error checking code.
    /*for (int i=0; i<n; i++) {
        // Calculate the actual probability of ending at index i.
        double cur_log = 0;
        for (int j=0; j<m; j++) {
            int idx = (i+j) % n;
            if (dna[idx] != match[j]) {
                if (probs[j] == 0) {
                    cur_log = 1;
                    break;
                }
                else if (probs[j] == 1) {
                    
                } else cur_log = cur_log + log(probs[j]);
            }
            else {
                if (probs[j] == 1) {
                    cur_log = 1;
                    break;
                }
                else if (probs[j] == 0) {

                }
                else cur_log = cur_log + log(1 - probs[j]);
            }
        }
        cd r = {0, 0};
        for (int j=0; j<m; j++) {
            int idx = m + i - 1 - j;
            r = r + fftmatch[j] * fftdna[idx];
        }
        bool matches = ((int)(res2[m+i-1].real() + 0.5) == n_requires);
        if (matches) {
            if (cur_log == 1) {
                cerr << "BAD 3" << endl;
            } else {
                float error = res[m+i-1].real() - cur_log;
                if (abs(error) > pow(10, -10)) {
                    cerr << "BAD 2 " << error << endl;
                }
            }
            // cerr << "Prob starting at " << i << ": " << "e^" << res[m + i - 1].real() << " Error: " << res[m+i-1].real() - cur_log << endl;
        }
        else if (cur_log != 1) {
            cerr << "BAD!" << endl;
        }
    }*/

    vector<pair<pair<bool, double>, int> > results;
    results.resize(n);
    for (int i=0; i<n; i++) {
        results[i].second = i;
        results[i].first.second = res[m+i-1].real();
        results[i].first.first = ((int)(res2[m+i-1].real() + 0.5) == n_requires);
    }

    // Sort
    sort (results.begin(), results.end(), special_comp);

    for (int i=0; i<3; i++) {
        if (i >= results.size() || results[i].first.first == false) break;
        if (i != 0) cout << " ";
        cout << results[i].second + 1;
    }
    cout << endl;

    for (int i=0; i<min(10, (int)results.size()); i++) {
        // Check for error bounds
        int from = results[i].second;
        double cur_log = 0;
        for (int j=0; j<m; j++) {
            int idx = (from+j) % n;
            if (dna[idx] != match[j]) {
                if (probs[j] == 0) {
                    cur_log = 1;
                    break;
                }
                else if (probs[j] == 1) {
                    
                } else cur_log = cur_log + log(probs[j]);
            }
            else {
                if (probs[j] == 1) {
                    cur_log = 1;
                    break;
                }
                else if (probs[j] == 0) {

                }
                else cur_log = cur_log + log(1 - probs[j]);
            }
        }
        if ((cur_log != 1) != (results[i].first.first)) {
            cerr << "BAD 1" << endl;
        }
        if (cur_log != 1) {
            double error = abs(cur_log - results[i].first.second);
            if (error > pow(10, -6)) {
                cerr << "BAD 2 " << error << endl;
            }
        }
    }

    for (int i=0; i < 50; i++) {
        // Choose a random position and see if the zarray failed.
        int pos = rand() % results.size();
        double cur_log = 0;
        for (int j=0; j<m; j++) {
            int idx = (results[pos].second+j) % n;
            if (dna[idx] != match[j]) {
                if (probs[j] == 0) {
                    cur_log = 1;
                    break;
                }
                else if (probs[j] == 1) {
                    
                } else cur_log = cur_log + log(probs[j]);
            }
            else {
                if (probs[j] == 1) {
                    cur_log = 1;
                    break;
                }
                else if (probs[j] == 0) {

                }
                else cur_log = cur_log + log(1 - probs[j]);
            }
        }
        if ((cur_log != 1) != (results[pos].first.first)) {
            cerr << "BAD 1" << endl;
        }

    }

    // Count possible checks
    int count = 0;
    for (int i=0; i<results.size(); i++) {
        if (results[i].first.first) count ++;
    }
    cerr << 100 * ((double)count / (double)results.size()) << "%" << endl;

    // See how much variation in the first 100 bits;
    cerr << results[0].first.second << " " << results[min(40, count-1)].first.second << endl;

    return 0;
}
