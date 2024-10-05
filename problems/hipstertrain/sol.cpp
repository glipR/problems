// Jackson Goerner (glipR in some places)
// HAS AN ISSUE: Sample output is incorrect. TODO: inspect.
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <queue>
#include <map>

#define X first
#define Y second

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;

template <typename T, typename U>
ostream& operator<< (ostream& out, const pair<T, U>& p) {
    out << '(';
    out << p.X << ", " << p.Y;
    out << ")";
    return out;
}

template <typename T>
ostream& operator<< (ostream& out, const vector<T>& v) {
    out << '[';
    for (auto o: v) { out << o << ", "; }
    out << "\b\b]";
    return out;
}

#define MAX_STATIONS 1001
#define MAX_HIPSTERS 10001

ll n_stations, init_capacity;
// size of train car
ll attach_capacities[MAX_STATIONS];
// number of hipsters
ll hipsters[MAX_STATIONS];
// how many leave the train
ll leaves[MAX_STATIONS];
// what pct they will stop boarding at
ll boarding_capacity[MAX_STATIONS];
// How large is the group that follows.
ll group_amount[MAX_STATIONS];

ll DP[MAX_STATIONS][MAX_HIPSTERS+1];
ll soln[MAX_STATIONS];

bool test_checking = false;

bool should_board(ll hipster_pct, ll current, ll capacity) {
    // We want to board if hipster_pct of capacity >= current.
    return current * 100 <= capacity * hipster_pct;
}

int main() {

    cin >> n_stations >> init_capacity;

    for (int i=0; i<n_stations; i++) {
        cin >> attach_capacities[i] >> hipsters[i] >> leaves[i] >> boarding_capacity[i] >> group_amount[i];
    }

    ll current_capacity = init_capacity + attach_capacities[0];
    for (int i=0; i<=MAX_HIPSTERS; i++) {
        // Set DP[0][i]
        if (i > hipsters[0]) DP[0][i] = -1;
        else if (i == 0) DP[0][i] = 0;
        else if (i * (group_amount[0] + 1) > current_capacity) DP[0][i] = -1;
        else {
            // Would the last hipster want to get on this train?
            ll total = (i-1) * (group_amount[0] + 1);
            DP[0][i] = should_board(boarding_capacity[0], total, current_capacity) ? (i * (group_amount[0] + 1)) : -1;
        }        
    }

    for (int i=1; i<n_stations; i++) {
        // Generate DP[i] from DP[i-1].
        ll available_hipsters = hipsters[i];
        // Attach the traincar
        current_capacity = current_capacity + attach_capacities[i];
        for (int j=0; j<=MAX_HIPSTERS; j++) {
            // We can just not pick anyone up.
            DP[i][j] = DP[i-1][j];
            // Everyone jumps off
            if (DP[i][j] != -1) DP[i][j] = max((ll)0, DP[i][j] - leaves[i]);
        }
        for (int k=0;;k++) {
            ll jump = 1 << k;
            if (jump > available_hipsters) break;
            available_hipsters = available_hipsters - jump;
            for (int j=MAX_HIPSTERS; j>=jump; j--) {
                // Try update DP[i][j] from DP[i][j-2^k]
                if (DP[i][j-jump] == -1) continue;
                // Can 2^k hipsters board?
                // Before the last hipster boards, this many occupy.
                ll total = (jump - 1) * (group_amount[i] + 1) + DP[i][j-jump];
                if (!should_board(boarding_capacity[i], total, current_capacity)) continue;
                // We can board
                total = total + (group_amount[i] + 1);
                if (total > current_capacity) continue;
                if (DP[i][j] == -1 || DP[i][j] > total) {
                    DP[i][j] = total;
                }
            }
        }
        if (available_hipsters == 0) continue;
        // Final stretch
        for (int j=MAX_HIPSTERS; j>=available_hipsters; j--) {
                // Try update DP[i][j] from DP[i][j-2^k]
                if (DP[i][j-available_hipsters] == -1) continue;
                // Can 2^k hipsters board?
                // Before the last hipster boards, this many occupy.
                ll total = (available_hipsters - 1) * (group_amount[i] + 1) + DP[i][j-available_hipsters];
                if (!should_board(boarding_capacity[i], total, current_capacity)) continue;
                // We can board
                total = total + (group_amount[i] + 1);
                if (total > current_capacity) continue;
                if (DP[i][j] == -1 || DP[i][j] > total) {
                    DP[i][j] = total;
                }
            }
    }

    ll best = -1;

    // Now, at the end of the day what's the largest j for which DP[n_stations-1][j] != -1
    for (int j=MAX_HIPSTERS; j>=0; j--) {
        if (DP[n_stations-1][j] != -1) {
            best = j;
            break;
        }
    }

    ll saved_best = best;
    ll total_hipsters = hipsters[0];

    // Now, backtrack to find the correct values;
    for (int i=n_stations-1; i>0; i--) {
        total_hipsters = total_hipsters + hipsters[i];
        // We need to pick somewhere between 0 and hipsters[i] people.
        for (int j=0; j<=hipsters[i]; j++) {
            if (DP[i-1][best - j] == -1) continue;
            // Can we get our capacity in DP[i][best] by adding j people at station i?
            ll total = (j - 1) * (group_amount[i] + 1) + max((ll)0, DP[i-1][best-j] - leaves[i]);
            if (!should_board(boarding_capacity[i], total, current_capacity)) continue;
            // We can board
            total = total + (group_amount[i] + 1);
            if (total == DP[i][best]) {
                soln[i] = j;
                break;
            }
        }
        best = best - soln[i];
        current_capacity = current_capacity - attach_capacities[i];
    }
    soln[0] = best;

    ll used_stations = 0;
    for (int i=0; i<n_stations; i++)
        used_stations = used_stations + (soln[i] > 0);

    if (test_checking) {
        cerr << "Used " << 100 * used_stations / (float)n_stations << "% of stations." << endl;
        cerr << "Used " << 100 * saved_best / total_hipsters << "% of hipsters." << endl;
    }

    for (int i=0; i<n_stations; i++) {
        cout << soln[i];
        if (i == n_stations-1) cout << endl;
        else cout << " ";
    }

    return 0;
}