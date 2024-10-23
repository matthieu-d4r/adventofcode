package day03

import (
	"bytes"
	"log"
	"os"
	"unicode"
)

func part1(filename string) int {
	data, err := os.ReadFile(filename)
	if err != nil {
		log.Fatalln(err)
	}

	var (
		schematic    = bytes.Fields(data)
		n, size, sum int
	)

	for i, row := range schematic {
		for j, b := range row {
			if unicode.IsDigit(rune(b)) {
				n = n*10 + int(b-'0')
				size++

				if j == len(row)-1 || !unicode.IsDigit(rune(row[j+1])) {
					if hasSymbolAround(i, j, size, schematic) {
						sum += n
					}
					n, size = 0, 0
				}
			}
		}
	}
	return sum
}

// -----------------------------------------------------------------------------

func hasSymbolAround(i, j, size int, m [][]byte) bool {
	for ii := i - 1; ii <= i+1; ii++ {
		if ii < 0 || ii > len(m)-1 {
			continue
		}
		for jj := j - size; jj <= j+1; jj++ {
			if jj < 0 || jj > len(m[ii])-1 || (ii == i && j-size < jj && jj < j+1) {
				continue
			}
			if b := m[ii][jj]; !unicode.IsDigit(rune(b)) && b != '.' {
				return true
			}
		}
	}
	return false
}
