package day02

import "unicode"

func isNotAlphanumeric(r rune) bool {
	return unicode.IsPunct(r) || unicode.IsSpace(r)
}
