package day03

import (
	"bytes"
	"log"
	"os"
	"strconv"
	"unicode"
)

func part2(filename string) int {
	data, err := os.ReadFile(filename)
	if err != nil {
		log.Fatalln(err)
	}

	var (
		schematic   = bytes.Fields(data)
		n1, n2, sum int
	)

	for i, row := range schematic {
		for j, b := range row {
			if b == '*' {
				n1, n2 = findNumbers(i, j, schematic)
				sum += n1 * n2
			}
		}
	}
	return sum
}

// -----------------------------------------------------------------------------

func findNumbers(i, j int, m [][]byte) (n1, n2 int) {
	for ii := i - 1; ii <= i+1; ii++ {
		if ii < 0 || ii > len(m)-1 {
			continue
		}
		for jj := j - 1; jj <= j+1; jj++ {
			if jj < 0 || jj > len(m[ii])-1 || (ii == i && jj == j) {
				continue
			}
			if unicode.IsDigit(rune(m[ii][jj])) {
				l, r := findNumber(jj, m[ii])
				if n1 == 0 {
					n1, _ = strconv.Atoi(string(m[ii][l:r]))
					jj = r
				} else {
					n2, _ = strconv.Atoi(string(m[ii][l:r]))
					return
				}
			}
		}
	}
	return
}

func findNumber(j int, row []byte) (int, int) {
	l, r := j-1, j+1
	for l >= 0 && unicode.IsDigit(rune(row[l])) {
		l--
	}
	for r < len(row) && unicode.IsDigit(rune(row[r])) {
		r++
	}
	return l + 1, r
}
