#include "testlib.h"
#include <iostream>

using namespace std;
typedef long long ll;

const ll MAX_AMOUNT = 1000000;
const ll MAX_HEARTS = 10000;
const ll MAX_TIME = 100000000;



int main(int argc, char* argv[]) {
    registerGen(argc, argv, 1);
    for (int testno=0; testno<atoi(argv[2]); testno++) {
        startTest(testno + atoi(argv[3]));
        ll b = atoi(argv[1]);
        ll p = rnd.next(min(3*b, (ll)MAX_AMOUNT));
        ll q = rnd.next(min(3*b, (ll)MAX_AMOUNT));
        cout << b << " " << p << " " << q << endl;
        // Generate trucks.
        for (ll i=0; i<p; i++) {
            ll x = rnd.next(b-1);
            ll y = rnd.next(b-1);
            ll l = rnd.next((ll)1,b);
            ll h = rnd.next((ll)1, (ll)MAX_HEARTS);
            cout << x << " " << y << " " << l << " " << h << endl;
        }
        // Number of spawns where we have any choice of time
        ll numLoops = rnd.next(min((ll)2, (ll)(b / 3)));
        // Generate spawns.
        for (ll i=0; i<q; i++) {
            ll x = rnd.next((ll)(b-1));
            ll y = rnd.next((ll)(b-1));
            ll t1 = rnd.next((ll)MAX_TIME);
            ll t2;
            if (i < numLoops) {
                t2 = t1 + rnd.next((ll)min((ll)b, (ll)MAX_TIME), (ll)MAX_TIME);
            } else {
                t2 = t1 + rnd.next((ll)(b-1));
            }
            cout << x << " " << y << " " << t1 << " " << t2 << endl;
        }
    }
}
