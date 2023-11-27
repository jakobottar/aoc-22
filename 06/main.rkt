#lang racket

(define (token? t)
    (equal? (check-duplicates t) #f))

(define (time-til-token f l)

    ; recursive helper function
    (define (helper m c)
        (cond
            [(empty? m) -1]
            [(token? (take m l)) c]
            [else (helper (rest m) (+ c 1))]))

    ; convert message to list of chars
    (let ([m (string->list (first (file->lines f)))])
        (helper m l)))
    
(printf "part 1 example: ~a\n" (time-til-token "example.txt" 4))
(printf "part 1: ~a\n" (time-til-token "input.txt" 4))

(printf "part 2 example: ~a\n" (time-til-token "example.txt" 14))
(printf "part 2: ~a\n" (time-til-token "input.txt" 14))