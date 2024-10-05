#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <queue>
#include <map>

using namespace std;

typedef long long ll;
typedef vector<ll> vll;
typedef pair<ll, ll> pl;
typedef vector<pl> vpl;

#define MAX_N 2000000

ll T, n_i;
vll fac, pr;
void fast_sieve(ll n) {
    fac.assign(n+1, 0);
    for (ll i=2; i<=n; i++) {
        if (fac[i] == 0) fac[i] = i, pr.push_back(i);
        for (ll p: pr) if (p > fac[i] || i * p > n) break; else fac[i * p] = p;
    }
}

vpl fast_factors(ll n) {
    vpl res;
    while (n > 1) {
        ll f = fac[n];
        n /= f;
        if (res.size() == 0 || res[res.size()-1].first != f) {
            res.push_back({f, 1});
        } else {
            res[res.size() - 1].second++;
        }
    }
    return res;
}

int main() {

    cin >> T;
    fast_sieve(MAX_N);

    for (int i=0; i<T; i++) {
        cin >> n_i;
        vpl factors = fast_factors(n_i);
        ll ways = 1;
        for (pl x: factors) {
            ways *= x.second + 1;
        }
        cout << ways << endl;
    }

    return 0;
}