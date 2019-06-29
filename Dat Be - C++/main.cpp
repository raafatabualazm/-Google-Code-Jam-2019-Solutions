#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n , b , f, t;
    cin >> t;
    string bits;
    string response;
    int k, l;
    vector<int> broken;
    vector<int> broken2;
    for (int i =0; i < t; i++)
    {
        bits.clear();
        broken.clear();
        cin >> n >> b >> f;
        for (int j = 0; j < n; j++)
        {
            if (j % 2 == 0) bits+= "1";
            else bits += "0";
        }
        cout << bits << endl;
        cout.flush();
        cin >> response;
        k = 0;
        l = 0;
        while (k < bits.length() && l < response.length())
        {
            if (bits[k] == response[l])
            {
                k++;
                l++;
            } else
            {
                broken.push_back(k);
                k++;
            }
        }
        for (auto elem : broken)
        {
            cout << elem << " ";
        }
        cout << endl;
        cout.flush();

    }
    return 0;
}
