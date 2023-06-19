package main

import (
	"encoding/json"
	"fmt"
	"log"
	"strings"
)

var sampleJSON = `[
	{"id": 1, "username": "john", "houseplants":10, "email": "john@example.com"},
	{"id": 2, "username": "jane", "houseplants": 4, "email": "jane@example.com"}
]`

func addAllInts(data []map[string]interface{}) int {
	sum := 0
	for _, item := range data {
		if intValue, ok := item["houseplants"].(float64); ok {
			sum += int(intValue)
		}
	}
	return sum
}

func main() {
	reader := strings.NewReader(sampleJSON)

	var data []map[string]interface{}
	err := json.NewDecoder(reader).Decode(&data)
	if err != nil {
		log.Println("Error decoding JSON:", err)
		return
	}

	total := addAllInts(data)
	fmt.Println("Total:", total)
}
