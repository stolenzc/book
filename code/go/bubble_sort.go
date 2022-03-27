package main

import "fmt"

func bubbleSort(arr []int) []int {
	for i := 0; i < len(arr); i++ {
		for j := 0; j < len(arr) - i - 1; j++ {
			if arr[j] > arr[j + 1] {
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
			}
		}
	}
	return arr
}

func main() {
	arr := []int{5, 2, 4, 6, 1, 3}
	bubbleSort(arr)
	fmt.Println(arr)
}