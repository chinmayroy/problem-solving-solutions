#include <iostream>
using namespace std;

int main() {
	int t;
	cin >> t;
	while(t--){
	    int n, x, y;
	    cin >> n >> x >> y;
	    
	    if((n+1)*y >= x) std::cout << "Yes" << std::endl;
	    else std::cout << "No" << std::endl;
	}
	return 0;
}
