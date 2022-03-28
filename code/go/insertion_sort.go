package main

import "fmt"

func insertionSort(arr []int){
	for i := 1; i < len(arr); i++ {
		current := arr[i]
		for j := i - 1; j >= 0; j-- {
			if current < arr[j]{
				arr[j+1] = arr[j]
			} else {
				arr[j+1] = current
				break
			}
			if j == 0 {
				arr[j] = current
			}
		}
	}
}

func main(){
	arr := []int{5, 2, 4, 6, 1, 3}
	insertionSort(arr)
	fmt.Println(arr)
}