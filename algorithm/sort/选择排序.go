package main

import (
	"fmt"
	"math/rand"
	"sort"
	"time"
)

// get_rand_slice 获取指定长度和指定范围的随机切片
func get_rand_slice(length, start, end int) (result []int) {
	for i := 0; i < length; i++ {
		item := rand.Intn(end-start) + start
		result = append(result, item)
	}
	return
}


// mySort 选择排序golang实现
func mySort(origin []int) []int {
	length := len(origin)
	for i:=0; i<length; i++{
		min := i
		for j:=i; j<length; j++{
			if origin[j] < origin[min]{
				min = j
			}
		}
		if min != i {
			origin[i], origin[min] = origin[min], origin[i]
		}
	}
	return origin
}


// compare 排序结果比较器
func compare(slice1, slice2 []int) bool {
	len_slice1 := len(slice1)
	len_slice2 := len(slice2)
	if len_slice1 != len_slice2{
		return false
	}
	length := len_slice1
	for i:=0; i<length; i++{
		if slice1[i] != slice2[i]{
			return false
		}
	}
	return true
}


func main(){
	for i:=0; i<20; i++{
		// 设置随机数种子，保证每次产生的数都不一样
		rand.Seed(time.Now().UnixNano())
		length := rand.Intn(20)
		origin := get_rand_slice(length, 0, 100)
		fmt.Printf("%v", origin)
		my_sort := mySort(origin[:])
		build_in_sort := origin[:]
		sort.Ints(build_in_sort)
		if result := compare(my_sort, build_in_sort); result==false{
			fmt.Print(result)
			fmt.Print("排序失败")
			break;
		}
	}
	fmt.Println("排序成功")
}
