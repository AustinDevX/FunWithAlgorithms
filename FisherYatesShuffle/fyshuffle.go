package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	nums := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	fyshuffle(nums)
	fmt.Println(nums)
}

// fyshuffle randomly shuffles a slice of integers in place
func fyshuffle(arr []int) {
	source := rand.NewSource(time.Now().UnixNano())
	randomizer := rand.New(source)
	for currentIndex := len(arr) - 1; currentIndex > 1; currentIndex-- {
		destIndex := randomizer.Int31n(int32(currentIndex + 1))
		arr[currentIndex], arr[destIndex] = bitSwap(arr[currentIndex], arr[destIndex])
	}
}

// ptrSwap accepts two integer pointers and swaps their values
func ptrSwap(a *int, b *int) {
	var temp = *a
	*a = *b
	*b = temp
}

// simpleSwap returns its two operands in reversed order
func simpleSwap(a int, b int) (int, int) {
	return b, a
}

// arithmeticSwap swaps the values of its operands using arithmetic
// It returns the swapped operans in the same order, may panic due to arithmetic overflow
func arithmeticSwap(a int, b int) (int, int) {
	a = a + b
	b = a - b
	a = a - b
	return a, b
}

// bitswap swaps the values of its operands using bit manipulation
// It returns the swapped operands
func bitSwap(a int, b int) (int, int) {
	a = a ^ b
	b = a ^ b
	a = a ^ b
	return a, b
}
