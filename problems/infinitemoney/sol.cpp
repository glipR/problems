// Works!

#include <iostream>
#include <string>
#include <map>
#include <vector>

#define FOR(x,a,b) for(int x=(a);x<(b);x++)
#define MAX(a, b) ((a) < (b) ? (b) : (a))
#define MAXPOSITION 128

using namespace std;

typedef long long ll;

ll INPUT1_MATRIX[MAXPOSITION][MAXPOSITION];
ll INPUT2_MATRIX[MAXPOSITION][MAXPOSITION];
ll RESULT_MATRIX[MAXPOSITION][MAXPOSITION];
ll ORIGINAL_MATRIX[MAXPOSITION][MAXPOSITION];

map<string, int> ids;

ll n, m, t;

void exponentiate(ll power) {
    FOR(x, 0, 1 << n)
        FOR(y, 0, 1 << n)
            INPUT1_MATRIX[x][y] = x != y ? -1000000000 : 0;
    FOR(x, 0, 1 << n)
        FOR(y, 0, 1 << n)
            INPUT2_MATRIX[x][y] = ORIGINAL_MATRIX[x][y];
    while (power) {
        if (power & 1) {
            FOR(x, 0, 1 << n)
                FOR(y, 0, 1 << n) {
                    ll maximum = -1000000000;
                    FOR(z, 0, 1 << n)
                        if (INPUT1_MATRIX[x][z] != -1000000000 && INPUT2_MATRIX[z][y] != -1000000000)
                            maximum = MAX(INPUT1_MATRIX[x][z] + INPUT2_MATRIX[z][y], maximum);
                    RESULT_MATRIX[x][y] = maximum;
                }
            FOR(x, 0, 1 << n)
                FOR(y, 0, 1 << n)
                    INPUT1_MATRIX[x][y] = RESULT_MATRIX[x][y];
        }
        FOR(x, 0, 1 << n)
            FOR(y, 0, 1 << n) {
                ll maximum = -1000000000;
                FOR(z, 0, 1 << n)
                    if (INPUT2_MATRIX[x][z] != -1000000000 && INPUT2_MATRIX[z][y] != -1000000000)
                        maximum = MAX(INPUT2_MATRIX[x][z] + INPUT2_MATRIX[z][y], maximum);
                RESULT_MATRIX[x][y] = maximum;
            }
        FOR(x, 0, 1 << n)
            FOR(y, 0, 1 << n)
                INPUT2_MATRIX[x][y] = RESULT_MATRIX[x][y];
        power /= 2;
    }
    FOR(x, 0, 1 << n)
        FOR(y, 0, 1 << n)
            RESULT_MATRIX[x][y] = INPUT1_MATRIX[x][y];
}

int main() {

    cin >> t;

    FOR(testno, 0, t) {

        cin >> n >> m;

        FOR(x, 0, 1 << n)
            FOR(y, 0, 1 << n)
                ORIGINAL_MATRIX[x][y] = x != y ? -1000000000 : 0;

        ids.clear();
        FOR(x, 0, n) {
            string id;
            cin >> id;
            ids[id] = x;
        }

        vector<int> required;
        vector<int> gets;
        ll lose;
        ll win;
        string tmp;

        FOR(x, 0, m) {
            lose = 0;
            required.clear();
            gets.clear();
            while (1) {
                cin >> tmp;
                if (tmp == "and") break;
                required.push_back(ids[tmp]);
            }
            cin >> lose;
            cin >> tmp; // gold
            cin >> tmp; // can
            cin >> tmp; // be
            cin >> tmp; // traded
            cin >> tmp; // for
            while (1) {
                cin >> tmp;
                if (tmp == "and") break;
                gets.push_back(ids[tmp]);
            }
            cin >> win;
            cin >> tmp; // gold
            // Figure out what positions we can make this trade at.
            FOR(i, 0, 1 << n) {
                bool can = true;
                FOR(j, 0, required.size()) {
                    if (!(i & (1 << required[j]))) {
                        can = false;
                    }
                }
                if (!can) continue;
                // Now apply the trade.
                int p = i;
                FOR(j, 0, required.size()) {
                    p = p - (1 << required[j]);
                }
                FOR(j, 0, gets.size()) {
                    p = p | (1 << gets[j]);
                }
                ORIGINAL_MATRIX[i][p] = MAX(win - lose, ORIGINAL_MATRIX[i][p]);
            }
        }

        // Just be safe - exponentiate large.
        exponentiate(2 * (1 << n));
        bool found = false;
        FOR(x, 0, 1 << n)
            if (RESULT_MATRIX[x][x] > 0)
                found = true;
        if (!found) {
            cout << 0 << endl;
            continue;
        }

        ll hi = 2 * (1 << n);
        ll lo = 0;
        while (hi - lo > 1) {
            ll mid = (hi + lo) / 2;
            exponentiate(mid);
            found = false;
            FOR(x, 0, 1 << n)
                if (RESULT_MATRIX[x][x] > 0) {hi = mid; found = true; break;}
            if (!found) lo = mid;
            /*cerr << mid << " " << found << endl;
            FOR(x1, 0, 1 << n) {
                FOR(x2, 0, 1 << n)
                    cerr << RESULT_MATRIX[x1][x2] << " ";
                cerr << endl;
            }*/
        }

        // hi should be the lowest time that a loop exists.
        cout << hi << endl;

    }

    return 0;
}