#lang racket

(define (get-common-item rucksack)
  (let* ([rucksack (string->list rucksack)]
         [first-half (take rucksack (/ (length rucksack) 2))] ; get the first half of the rucksack
         [second-half (drop rucksack (/ (length rucksack) 2))] ; drop the first half of the rucksack
         [first-half-set (list->set first-half)] ; convert the halves into sets
         [second-half-set (list->set second-half)])

    (let* ([common (first (set->list (set-intersect first-half-set
                                                    second-half-set)))] ; get the common item
           [common (char->integer common)]) ; convert to integer
      (if (> common (char->integer #\Z)) ; if the item is lowercase
          (- common (char->integer #\a) -1) ; return 1-26
          (- common (char->integer #\A) -27))))) ; else return 27-52

(define (get-common-item-among-three rucksacks)
  (define (helper input scores)

    (cond
      [(empty? input) scores]
      [(let* ([three (take input 3)]
              [more (drop input 3)]
              [sets (map list->set (map string->list three))]
              [common (char->integer (first (set->list (apply set-intersect sets))))]
              [score (if (> common (char->integer #\Z))
                              (- common (char->integer #\a) -1)
                              (- common (char->integer #\A) -27))])

         (helper more (cons score scores)))]))

  (helper rucksacks empty))

(printf "part 1 example: ~a\n" (apply + (map get-common-item (file->lines "example.txt"))))
(printf "part 1: ~a\n" (apply + (map get-common-item (file->lines "input.txt"))))

(printf "part 2 example: ~a\n" (apply + (get-common-item-among-three (file->lines "example.txt"))))
(printf "part 2: ~a\n" (apply + (get-common-item-among-three (file->lines "input.txt"))))
