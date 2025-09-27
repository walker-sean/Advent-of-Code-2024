#lang racket

(define file-in (open-input-file "input"))

(define l1 '())
(define l2 '())

(define (process-file file)
  (define line (read-line file))
  (match line
    ["" 0]
    [_
     #:do
    ))

(close-input-port file-in)