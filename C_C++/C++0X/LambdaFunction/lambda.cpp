#include <iostream>
#include <vector>
#include <string>
#include <utility>
#include <algorithm>

using namespace std;
typedef pair<int, int> int_pair;

bool sort_pair_1st (int_pair p1, int_pair p2) { return (p1.first < p2.first); }
bool sort_pair_2nd (int_pair p1, int_pair p2) { return (p1.second < p2.second); }
void print_vector(vector<int_pair> v, string s=".........")
{
    cout << s << endl;
    for(auto i: v) {
        cout << i.first << ":" << i.second << endl;
    }
    cout << "===================================" << endl;

}

int main()
{
    vector<int_pair> v;
    int x = 10;

    v.push_back(make_pair(1,12));
    v.push_back(make_pair(12,1));
    v.push_back(make_pair(4,3));    
    v.push_back(make_pair(6,4));
    v.push_back(make_pair(3,2));

    print_vector(v, "Original vector");

    sort(v.begin(), v.end(), sort_pair_1st);    
    print_vector(v, "Sort 1st");
    
    sort(v.begin(), v.end(), sort_pair_2nd);
    print_vector(v, "Sort 2nd");
    
    sort(v.begin(), v.end(), [](int_pair p1, int_pair p2) {return (p1.first < p2.first);});
    print_vector(v, "Sort 1st using lambda");
    
    sort(v.begin(), v.end(), [x](int_pair p1, int_pair p2) -> bool {x*2; return (p1.second < p2.second);});
    print_vector(v, "Sort 2nd using lambda");
    
    return 0;
}
