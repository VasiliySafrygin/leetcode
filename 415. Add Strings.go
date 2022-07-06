package main

import (
	"fmt"
)

func max(n1 int, n2 int) int {
    if (n1 > n2) {
		return n1;
	} else {
		return n2;
	}
}

func addStrings(num1 string, num2 string) string {
	max_len := max(len(num1), len(num2))
	for i := 0; i < max_len; i++ {
		fmt.Printf("I %d\n", i);
		fmt.Printf("1 %d\n", int(num1[i]));
		try {
			fmt.Printf("2 %d\n", int(num2[i]));
		}
	}	
	return "";
}


func main() {
	addStrings("123", "34");
}