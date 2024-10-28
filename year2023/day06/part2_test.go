package day06

import "testing"

func TestPart2(t *testing.T) {
	testCases := []struct {
		filename string
		want     int
	}{
		{"example.txt", 71503},
		{"puzzle_input.txt", 27102791},
	}
	for _, tc := range testCases {
		t.Run(tc.filename, func(t *testing.T) {
			if got := part2(tc.filename); got != tc.want {
				t.Errorf("got %v; want %v", got, tc.want)
			}
		})
	}
}
