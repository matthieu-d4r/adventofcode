package day04

import (
	"bufio"
	"log"
	"math"
	"os"
	"slices"
	"strings"
)

func part1(filename string) int {
	f, err := os.Open(filename)
	if err != nil {
		log.Fatalln(err)
	}
	defer f.Close()

	var (
		scanner           = bufio.NewScanner(f)
		tokens            []string
		sep, matches, sum int
	)

	for scanner.Scan() {
		tokens = strings.Fields(scanner.Text())

		sep = slices.Index(tokens, "|")
		matches = countMatches(tokens[2:sep], tokens[sep+1:])

		sum += int(math.Pow(2, float64(matches-1)))
	}
	return sum
}
