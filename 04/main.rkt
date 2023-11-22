#lang racket

(define (fully-overlap pairs)
  (let* ([pairs (string-split pairs ",")]
         [s1 (apply inclusive-range (map string->number (string-split (first pairs) "-")))]
         [s2 (apply inclusive-range (map string->number (string-split (second pairs) "-")))])

    (if (or (subset? s1 s2) (subset? s2 s1)) 1 0)))

(define (partial-overlap pairs)
  (let* ([pairs (string-split pairs ",")]
         [s1 (list->set (apply inclusive-range
                               (map string->number (string-split (first pairs) "-"))))]
         [s2 (list->set (apply inclusive-range
                               (map string->number (string-split (second pairs) "-"))))])

    ; don't forget to use set-op when applying procs to sets!
    (if (set-empty? (set-intersect s1 s2)) 0 1)))

(printf "part 1 example: ~a\n" (apply + (map fully-overlap (file->lines "example.txt"))))
(printf "part 1: ~a\n" (apply + (map fully-overlap (file->lines "input.txt"))))

(printf "part 2 example: ~a\n" (apply + (map partial-overlap (file->lines "example.txt"))))
(printf "part 2: ~a\n" (apply + (map partial-overlap (file->lines "input.txt"))))
