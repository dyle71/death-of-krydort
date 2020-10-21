# death-of-krydort

**The not entirely surprising death of Krydort Wolvirry, merchant of 
Kaedwen, finding himself suddenly floating in the North Sea alongside a 
ship of undead Nilfgardians.**

A Table-Top Witcher 3 RPG Dice game system evaluator

## Rationale

I'm part of a small RPG group and we are currently running the Witcher 3
table-top RPG game: https://rtalsoriangames.com/witcher-trpg.

However, we were quite dissatisfied and unconvinced on the original game
mechanics rolling a single D10 to resolve challenges.

In particular, I'm playing a merchant of Kaedwen, who is ... well ...
physically not really suited. Basically he good with his wits and can
convince anyone to buy anything. 

Full stop.

Yet, all of a sudden he finds himself in the middle of a storm at sea next
to a Nilfgardian galleon, full of undead warriors. Before he can climb up
the ship he simply needs to survive and swim to the vessel.

The original gameplay states: attribute + skill + D10 > 14 to succeed.

Krydort has a BODY attribute of 6 and an Athletics skill of 0, making the
act of swimming somehow demanding.

This tiny program tries to evaluate different alternatives to:

**The not entirely surprising death of Krydort Wolvirry, merchant of 
Kaedwen, finding himself suddenly floating in the North Sea alongside a 
ship of undead Nilfgardians.**

## Running krydort

To check if Krydort succeeds a swimming role, which resorts to "Atheltics"
do a

```
$ python3 -m krydort --probes 100000 --mode normal --luck 1 Athletics
Checking "Athletics" (DEX): attribute value = 6, skill value = 2
Game mode: normal - LUCK spend: 1
DC-level           minimum        failures          f-rate         success          s-rate         fumbles        critical
easy                    10           10045            0.10           89955            0.90           10045            9982
average                 14           50246            0.50           49754            0.50           10045            9982
challenging             18           90018            0.90            9982            0.10           10045            9982
difficult               20           91006            0.91            8994            0.09           10045            9982
impossible              30           99099            0.99             901            0.01           10045            9982
```

Whereas: 
* `minium` lists the value one has to be greater to
* `f-rate` is the failure rate
* `s-rate` is the success rate 


---

(C) Copyright 2020  
Oliver Maurhart, oliver.maurhart@headcode.space  
headcode.space e.U., https://www.headcode.space
