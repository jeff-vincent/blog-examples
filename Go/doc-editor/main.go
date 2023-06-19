package main

import (
	"log"
	"net/http"
	"sync"

	"github.com/gin-gonic/gin"
	"github.com/gorilla/websocket"
)

type Document struct {
	sync.RWMutex
	content string
	clients map[*websocket.Conn]bool
}

func main() {
	router := gin.Default()
	document := NewDocument()
	upgrader := websocket.Upgrader{
		CheckOrigin: func(r *http.Request) bool {
			return true // Allow all origins
		},
	}

	router.GET("/ws", handleWebSocket(document, &upgrader))

	err := router.Run(":8000")
	if err != nil {
		log.Fatal("Error starting server:", err)
	}
}

func NewDocument() *Document {
	return &Document{
		clients: make(map[*websocket.Conn]bool),
	}
}

func handleWebSocket(document *Document, upgrader *websocket.Upgrader) gin.HandlerFunc {
	return func(c *gin.Context) {
		conn, err := upgrader.Upgrade(c.Writer, c.Request, nil)
		if err != nil {
			log.Println("Error upgrading connection to WebSocket:", err)
			return
		}

		// Register client
		document.Lock()
		document.clients[conn] = true
		document.Unlock()

		// Handle incoming messages
		go handleIncomingMessages(document, conn)
	}
}

func handleIncomingMessages(document *Document, conn *websocket.Conn) {
	for {
		_, message, err := conn.ReadMessage()
		if err != nil {
			log.Println("Error reading WebSocket message:", err)

			// Unregister client
			document.Lock()
			delete(document.clients, conn)
			document.Unlock()

			// Close the connection
			conn.Close()
			break
		}

		document.Lock()
		if len(message) > 0 {
			document.content = string(message)
		} else {
			// Replace empty message with sample text
			document.content = "Start typing ..."
		}
		document.Unlock()

		document.RLock()
		for client := range document.clients {
			err := client.WriteMessage(websocket.TextMessage, []byte(document.content))
			if err != nil {
				log.Println("Error sending message to client:", err)
				client.Close()
				delete(document.clients, client)
			}
		}
		document.RUnlock()
	}
}
