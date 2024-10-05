// Currently has some overflow issues.
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <queue>
#include <map>

#define MOD 1000000007
#define MAX_FACT 10000
#define MAX_N 100000000000000
#define MAX_K 10

using namespace std;

typedef long long ll;
typedef vector<ll> vll;
typedef pair<ll, ll> pl;
typedef vector<pl> vpl;

ll fact[MAX_FACT+1];

map<ll, ll> DP[MAX_K];

ll expmod(ll a, ll b) {
    ll res=1%MOD;
    a %= MOD;
    for (; b; b /= 2) {
        if (b&1) {
            res=(res*a)%MOD;
        }
        a=(a*a)%MOD;
    }
    return res;
}

ll inv(ll a) {
    return expmod(a, MOD-2);
}

vpl slow_factors(ll a) {
    vpl res;
    for (ll i=2; i*i<=a; i++) if (a % i == 0) {
        res.push_back({i, 0});
        while (a % i == 0) {
            a /= i;
            res[res.size()-1].second++;
        }
    }
    if (a > 1) res.push_back({a, 1});
    return res;
}

ll nCk(ll a, ll b) {
    // b (num distinct - 1) is always quite small <= 10000.
    if (b > MAX_FACT) {
        // Problem!
        return -1;
    }
    if (a > MAX_FACT) {
        ll res = 1;
        for (ll i=0; i<b; i++) {
            res = (res * (a - i)) % MOD;
        }
        res = (res * inv(fact[b])) % MOD;
        return res;
    }
    return ((fact[a] * inv(fact[b]) % MOD) * inv(fact[a-b])) % MOD;
}

ll solve(ll n, vpl fac_counts, ll k, ll l=0) {
    if (k == 0) return 1;
    if (DP[k].count(n) > 0) return DP[k][n];
    ll total = 0;
    vll counters;
    counters.assign(fac_counts.size(), 0);
    vpl new_counts;
    new_counts.assign(fac_counts.size(), {0, 0});
    while (counters[0] <= fac_counts[0].second) {
        ll cur = n;
        for (int i=0; i<fac_counts.size(); i++) {
            for (int j=0; j<counters[i]; j++) {
                cur /= fac_counts[i].first;
            }
            new_counts[i] = {fac_counts[i].first, fac_counts[i].second - counters[i]};
        }
        ll distinct = solve(cur, new_counts, k-1, l+1);
        // for (int j=0; j<l; j++) cerr << "  ";
        // cerr << cur << " " << k-1 << " " << distinct << " " << total << " " << n / cur << endl;
        /*cerr << cur << " [";
        for (int i=0; i<new_counts.size(); i++) {
            cerr << "(" << new_counts[i].first << ", " << new_counts[i].second << "), ";
        }
        cerr << "]" << endl;*/
        if (distinct == 1)
            total = (total + 1) % MOD;
        else
            total = (total + nCk(n / cur + distinct - 1, distinct - 1)) % MOD;
        ll c = counters.size() - 1;
        counters[c] ++;
        while (c >= 1 && counters[c] > fac_counts[c].second) {
            counters[c] = 0;
            c--;
            counters[c]++;
        }
    }
    DP[k][n] = total;
    // cerr << n << " " << k << " " << DP[k][n] << endl;
    return DP[k][n];
}

int main() {

    fact[0] = 1;
    fact[1] = 1;
    for (int i=2; i<MAX_FACT+1; i++) {
      fact[i] = (fact[i-1] * i) % MOD;
    }

    ll n, k;

    cin >> n >> k;

    vpl res = slow_factors(n);

    for (int i=0; i<=k; i++) {
        DP[i].clear();
    }

    cout << solve(n, res, k) << endl;

    return 0;
}