#lang racket

(define (score-p1 line)
  (let ([theirs (- (char->integer (string-ref line 0)) (char->integer #\A))] ; code of their letter
        [mine (- (char->integer (string-ref line 2)) (char->integer #\X))]) ; code of my letter
    (+ (case (modulo (- mine theirs) 3)
         [(0) 3] ; draw
         [(1) 6] ; win
         [(2) 0]) ; lose
       mine 1))) ; add score for my letter

(define (score-p2 line)
  (let* ([theirs (- (char->integer (string-ref line 0)) (char->integer #\A))] ; code of their letter
         [result (- (char->integer (string-ref line 2)) (char->integer #\X))] ; code of the result
         [mine (modulo (+ theirs result -1) 3)]) ; code of my letter (p1's mod table but reverse)

    (+ (* result 3) mine 1))) ; add score for my letter

(printf "part 1 example: ~a\n" (apply + (map score-p1 (file->lines "example.txt"))))
(printf "part 1: ~a\n" (apply + (map score-p1 (file->lines "input.txt"))))

(printf "part 2 example: ~a\n" (apply + (map score-p2 (file->lines "example.txt"))))
(printf "part 2: ~a\n" (apply + (map score-p2 (file->lines "input.txt"))))
