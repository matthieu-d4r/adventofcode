package day04

import "strconv"

func countMatches(winning []string, draw []string) int {
	var (
		set        = make(map[int]struct{})
		n, matches int
	)

	for _, s := range winning {
		n, _ = strconv.Atoi(s)
		set[n] = struct{}{}
	}
	for _, s := range draw {
		n, _ = strconv.Atoi(s)
		if _, ok := set[n]; ok {
			matches++
		}
	}
	return matches
}
