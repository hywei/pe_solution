
_sum :: (Integral a) => [a] -> a
_sum = foldl step 0 
    where step x y = if (y `mod` 3 == 0 || y `mod` 5 == 0) then x + y else x

res = _sum [0..999]    