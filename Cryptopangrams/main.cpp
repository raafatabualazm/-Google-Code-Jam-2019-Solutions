#include <bits/stdc++.h>

using namespace std;
const int N = 2e6 + 5;
bitset<N> primes;

long double ratioP;
long double ratioP2;
int t;
uint64_t n;
int l;
uint64_t fact1;
uint64_t fact2;
uint64_t cypher[2000];
uint64_t decypher[2000];
set<uint64_t> letters;
map<uint64_t, char> letters2;
int b = 0;
void sieve()
{
    primes.set();
    primes[0] = primes[1] = 0;
    for (uint64_t  i = 2; i*i < N; i++)
    {
        if (primes[i] == 0) continue;
        else
        {
            for (uint64_t j = i*i; j < N; j += i)
            {
                primes[j] = 0;
            }
        }
    }
}
void tryPath(uint64_t factor)
{
    uint64_t decypher2[2000];
    decypher2[0] = factor;

    for (uint64_t m = 0; m < l; m++)
            {
                if (cypher[m] % decypher2[m] != 0) return;
                decypher2[m + 1] = cypher[m] / decypher2[m];
                //letters.insert(decypher[m + 1]);
            }
    for (uint64_t p = 0; p < l+1; p++) {
        decypher[p] = decypher2[p];
        letters.insert(decypher2[p]);
    }
}
int main()
{
    sieve();
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        //fill(cypher, cypher+101, 0);
        //fill(decypher, decypher+101, 0);
        letters.clear();
        letters2.clear();
        b = 0;
        cin >> n >> l;
        for (int j = 0; j < l; j++)
        {
            cin >> cypher[j];
        }
        if (cypher[0] % 2 == 0)
        {
            fact1 = 2;
            fact2 = cypher[0] / 2;
        }
        else for (uint64_t k = 3; k*k <= cypher[0]; k += 2)
        {
            if (primes[k] == 0) continue;
            else if (cypher[0] % k == 0)
            {
                fact1 = k;
                fact2 = cypher[0] / k;
                break;
            }

        }
        tryPath(fact1);
        tryPath(fact2);
//        ratioP = (long double)cypher[1]/fact1;
//        ratioP2 = (long double)cypher[1]/fact2;
//        if (ratioP == (int)ratioP)
//        {
//            decypher[0] = fact2;
//            decypher[1] = fact1;
//            letters.insert(decypher[0]);
//            letters.insert(decypher[1]);
//
//        } else if (ratioP2 == (int)ratioP2)
//        {
//            decypher[0] = fact1;
//            decypher[1] = fact2;
//            letters.insert(decypher[0]);
//            letters.insert(decypher[1]);
//        }
//        for (uint64_t m = 1; m < l; m++)
//            {
//                decypher[m + 1] = cypher[m] / decypher[m];
//                letters.insert(decypher[m + 1]);
//            }

        cout << endl;
        for (auto elem : letters)
        {
            letters2[elem] = 'A' + b;
            b++;
        }
        cout << "Case #" << i + 1 << ": ";
        for (int o = 0; o < l+1; o++)
        {
            cout << letters2[decypher[o]];
        }
        cout << endl;
    }
}
