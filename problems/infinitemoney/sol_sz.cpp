#include <bits/stdc++.h>
using namespace std;
map<string, int> imap = {
  {"amulet", 0},
  {"sword",  1},
  {"axe",    2},
  {"armor",  3},
  {"poison", 4},
  {"dirt",   5},
  {"steel",  6},
};
struct offer {
  int loseg, losemsk, getg, getmsk;
};
const int INF = 1000000000;
vector<offer> offers;
int n, m, cnum, maskn;
int mat[2][1<<7][1<<7], t[1<<7][1<<7];

int sol() {
  for (int i=0; i<(1<<7); i++)
  for (int j=0; j<m; j++) if ((i & (offers[j].losemsk)) == offers[j].losemsk) {
    int newmask = (i^offers[j].losemsk) | offers[j].getmsk;
    t[i][newmask] = max(t[i][newmask], offers[j].getg - offers[j].loseg);
  }
  // for (int i=0; i<(1<<7); i++)
  // for (int j=0; j<(1<<7); j++)
  // if (t[i][j] != -INF)
  //   printf("t(%d, %d) get %d\n", i, j, t[i][j]);

  for (int s=0; s<(1<<7); s++) {
    int cur = s%2;
    int nxt = (s+1)%2;

    for (int i=0; i<(1<<7); i++)
    for (int j=0; j<(1<<7); j++) {
      mat[nxt][i][j] = -INF;
      for (int k=0; k<(1<<7); k++)
      if (t[k][j] != -INF && mat[cur][i][k] != -INF) {
        int newv = mat[cur][i][k] + t[k][j];
        // if (newv > mat[nxt][i][j])
        //   printf("(%d, %d, %d) (%d) from (%d, %d, %d) (%d) + (%d, %d) (%d)\n",
        //     s+1, i, j, newv,
        //     s, i, k, mat[cur][i][k],
        //     k, j, t[k][j]);

        mat[nxt][i][j] = max(mat[nxt][i][j], newv);
      }
    }

    for (int i=0; i<(1<<7); i++) if (mat[nxt][i][i] > 0) return s+1;
  }
  return 0;
}

void reset() {
  maskn = 0;
  offers.clear();
  for (int i=0; i<(1<<7); i++) {
    for (int j=0; j<(1<<7); j++)  {
      mat[0][i][j] = -INF,
      mat[1][i][j] = -INF;
      t[i][j] = -INF;
    }
    mat[0][i][i] = 0;
    mat[1][i][i] = 0;
  }
}

int main() {
  // freopen("1.in", "r", stdin);
  cin >> cnum;
  while(cnum--) {
    string token;
    reset();
    cin >> n >> m;
    for (int i=0; i<n; i++) {
      cin >> token;
      maskn |= imap[token];
    }
    offers.resize(m);
    for (int i=0; i<m; i++) {
      offers[i] = {0, 0, 0, 0};
      while (true) {
        cin >> token;
        if (token == "and") break;
        offers[i].losemsk |= 1<<imap[token];
      }
      cin >> offers[i].loseg;
      cin >> token;   // gold

      cin >> token;   // can
      cin >> token;   // be
      cin >> token;   // traded 
      cin >> token;   // for
      while (true) {
        cin >> token;
        if (token == "and") break;
        offers[i].getmsk |= 1<<imap[token];
      }
      cin >> offers[i].getg;
      cin >> token;   // gold
    }
    cout << sol() << endl;
  }
  return 0;
}
