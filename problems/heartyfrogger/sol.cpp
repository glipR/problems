#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>

#define X first
#define Y second

using namespace std;

typedef long long ll;

// Dynamic RQ, with lazy propogation (Ranged updates.)
// Updates and querys are INCLUSIVE ON BOTH SIDES [L, R].
template<typename T, typename U> struct SegmentTree {
    int S, H;

    T z;
    vector<T> v; // Actual values (May not be up to date)

    U noop; // No Operation constant
    vector<bool> d; // Dirty array (What needs updating)
    vector<U> p; // Lazy propogated updates.

    SegmentTree<T, U>(int _S, T _z = T(), U _noop = U()) {
        z = _z, noop = _noop;
        for (S = 1, H = 1; S < _S; ) S *= 2, H++;
        v.resize(2*S, z);
        d.resize(2*S, false);
        p.resize(2*S, noop);
    }

    void set_leaves(vector<T> &l) {
        copy(l.begin(), l.end(), v.begin() + S);
        for (int i = S - 1; i > 0; i--)
            v[i] = v[2 * i] + v[2 * i + 1];
    }

    void apply(int i, U &up) {
        v[i] = up(v[i]);
        if(i < S) {
            p[i] = p[i] + up;
            d[i] = true;
        }
    }

    void rebuild(int i) {
        for (int l = i/2; l; l /= 2) {
            T c = v[2*l] + v[2*l+1];
            v[l] = p[l](c);
        }
    }

    void prop(int i) {
        for (int h = H; h > 0; h--) {
            int l = i >> h;

            if (d[l]) {
                apply(2*l, p[l]);
                apply(2*l+1, p[l]);

                p[l] = noop;
                d[l] = false;
            }
        }
    }

    void upd(int i, int j, U update) {
        i += S, j += S;
        prop(i), prop(j);

        for (int l = i, r = j; l <= r; l /= 2, r /= 2) {
            if((l&1) == 1) apply(l++, update);
            if((r&1) == 0) apply(r--, update);
        }

        rebuild(i), rebuild(j);
    }

    T query(int i, int j){
        i += S, j += S;
        prop(i), prop(j);

        T res_left = z, res_right = z;
        for(; i <= j; i /= 2, j /= 2){
            if((i&1) == 1) res_left = res_left + v[i++];
            if((j&1) == 0) res_right = v[j--] + res_right;
        }
        return res_left + res_right;
    }
};

struct maxNode {
    ll maxim;

    maxNode operator+(const maxNode &n) {
        return { max(n.maxim, maxim) };
    }
};

struct maxUpdate {
    bool type; // true => increment; false => set.
    ll value;

    maxNode operator()(const maxNode &n) {
        return { type ? n.maxim + value : value };
    }

    maxUpdate operator+(const maxUpdate &u) {
        if (type) {
            return { u.type, u.value + value};
        }
        return { type, value };
    }
};

const maxNode maxZero { 0 };
const maxUpdate maxNoUp { true, 0 };

template <typename T>
ostream& operator<< (ostream& out, const vector<T>& v) {
    out << '[';
    for (auto o: v) { out << o << ", "; }
    out << "\b\b]";
    return out;
}


struct Truck {
    ll x, y, l, h;

    bool operator < (const Truck& other) const {
        if (y == other.y) return x > other.x;
        return y > other.y;
    }
};

struct Spawn {
    ll x, y, t1, t2;

    bool operator < (const Spawn& other) const {
        if (y == other.y) return x > other.x;
        return y > other.y;
    }
};

ostream& operator<< (ostream& out, const Truck& t) {
    out << '(';
    out << t.x << ", " << t.y << "," << t.l << "," << t.h;
    out << ")";
    return out;
}

ostream& operator<< (ostream& out, const Spawn& t) {
    out << '(';
    out << t.x << ", " << t.y << "," << t.t1 << "," << t.t2;
    out << ")";
    return out;
}

int main() {

    ll b, p, q;
    cin >> b >> p >> q;

    vector<Truck> trucks(p);
    vector<Spawn> spawns(q);

    for (int i=0; i<p; i++) {
        cin >> trucks[i].x >> trucks[i].y >> trucks[i].l >> trucks[i].h;
    }
    for (int i=0; i<q; i++) {
        cin >> spawns[i].x >> spawns[i].y >> spawns[i].t1 >> spawns[i].t2;
    }

    // Sort trucks & Spawns
    sort(trucks.begin(), trucks.end());
    sort(spawns.begin(), spawns.end());

    SegmentTree<maxNode, maxUpdate> heartCount(b, maxZero, maxNoUp);
    vector<maxNode> nodeList(b);
    for (int i=0; i<b; i++) nodeList[i].maxim = 0;
    heartCount.set_leaves(nodeList);

    ll bestHearts = 0;
    int truckIndex = 0;
    int spawnIndex = 0;
    for (int y=b-1; y>=0; y--) {
        // First, add all trucks to the heartCount.
        while (truckIndex < p && trucks[truckIndex].y >= y) {
            int start = (((trucks[truckIndex].x - (b-1-y)) % b) + b) % b;
            int end = (((start + trucks[truckIndex].l - 1) % b) + b) % b;
            if (start <= end) {
                heartCount.upd(start, end, { true, trucks[truckIndex].h });
            } else {
                heartCount.upd(0, end, { true, trucks[truckIndex].h });
                heartCount.upd(start, b-1, { true, trucks[truckIndex].h });
            }
            truckIndex ++;
        }
        // Next, go through for each spawn point.
        while (spawnIndex < q && spawns[spawnIndex].y >= y) {
            bool wholeWayRound = false;
            if (spawns[spawnIndex].t2 - spawns[spawnIndex].t1 >= b) wholeWayRound = true;
            if (wholeWayRound) {
                bestHearts = max(bestHearts, heartCount.query(0, b-1).maxim);
                // cerr << spawns[spawnIndex] << " has total line with ";
                // cerr << heartCount.query(0, b-1).maxim << endl;
            } else {
                int t1 = ((spawns[spawnIndex].t1 % b) + b) % b;
                int t2 = ((spawns[spawnIndex].t2 % b) + b) % b;
                int end = (((spawns[spawnIndex].x - t1 - (b-1-y)) % b) + b) % b;
                int start = (((spawns[spawnIndex].x - t2 - (b-1-y)) % b) + b) % b;
                if (start <= end) {
                    bestHearts = max(heartCount.query(start, end).maxim, bestHearts);
                    // cerr << spawns[spawnIndex] << " has " << start << " " << end << " with ";
                    // cerr << heartCount.query(start, end).maxim << endl;
                } else {
                    bestHearts = max(heartCount.query(0, end).maxim, bestHearts);
                    bestHearts = max(heartCount.query(start, b-1).maxim, bestHearts);
                    // cerr << spawns[spawnIndex] << " has " << start << " " << end << " with ";
                    // cerr << max(heartCount.query(0, end).maxim, heartCount.query(start, b-1).maxim) << endl;
                }
            }
            spawnIndex ++;
        }
    }

    cout << bestHearts << endl;

    return 0;
}
