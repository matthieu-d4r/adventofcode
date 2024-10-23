package day04

import (
	"bufio"
	"log"
	"os"
	"slices"
	"strconv"
	"strings"
)

func part2(filename string) int {
	f, err := os.Open(filename)
	if err != nil {
		log.Fatalln(err)
	}
	defer f.Close()

	var (
		scanner                   = bufio.NewScanner(f)
		scratchcards              = make(map[int]int)
		tokens                    []string
		sep, matches, cardId, sum int
	)

	for scanner.Scan() {
		tokens = strings.Fields(scanner.Text())

		sep = slices.Index(tokens, "|")
		matches = countMatches(tokens[2:sep], tokens[sep+1:])
		cardId, _ = strconv.Atoi(tokens[1][:len(tokens[1])-1])

		scratchcards[cardId]++
		for i := 1; i <= matches; i++ {
			scratchcards[cardId+i] += scratchcards[cardId]
		}
		sum += scratchcards[cardId]
	}
	return sum
}
