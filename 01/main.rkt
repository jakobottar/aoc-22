#lang racket
(require racket/list)

(define (count-calories input)
  (define (helper input acc output)

    (cond
      [(empty? input) (cons acc output)] ; if empty, append final accumulation and exit
      [(string=? (first input) "")
       (helper (rest input) 0 (cons acc output))] ; if empty list, push acc into output, reset acc
      [else
       (set! acc (+ acc (string->number (first input)))) ; else, add to acc
       (helper (rest input) acc output)] ; recall on rest of list
      ))

  (helper input 0 empty))

(printf "part 1 example: ~a\n" (apply max (count-calories (file->lines "example.txt"))))
(printf "part 1: ~a\n" (apply max (count-calories (file->lines "input.txt"))))

(printf "part 2 example: ~a\n" (apply + (take (sort (count-calories (file->lines "example.txt")) > ) 3)))
(printf "part 2: ~a\n" (apply + (take (sort (count-calories (file->lines "input.txt")) > ) 3)))