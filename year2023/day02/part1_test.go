package day02

import "testing"

func TestPart1(t *testing.T) {
	testCases := []struct {
		filename string
		want     int
	}{
		{"example.txt", 8},
		{"puzzle_input.txt", 2476},
	}
	for _, tc := range testCases {
		t.Run(tc.filename, func(t *testing.T) {
			if got := part1(tc.filename); got != tc.want {
				t.Errorf("got %v; want %v", got, tc.want)
			}
		})
	}
}
