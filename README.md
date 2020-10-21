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

Krydort has a DEX attribute of 6 and an Athletics skill of 2, making the
act of swimming _somehow_ demanding.

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

The current house rules are:

* `normal`: as in the books...
* `house1`: a fumble is only when the next role reveals > 5 and luck adds a D6.
* `house2`: instead of D10 we use 2*D5, luck adds an additional D5 to the initial pool.


Now, Krydort is really a louse swimmer. So, these rules give:

Mode: *normal* with 1 luck:
```
$ python3 -m krydort --probes 100000 --mode normal --luck 1 Athletics
Checking "Athletics" (DEX): attribute value = 6, skill value = 2
Game mode: normal - LUCK spend: 1
DC-level           minimum        failures          f-rate         success          s-rate         fumbles        critical
easy                    10            9989            0.10           90011            0.90            9989            9934
average                 14           49919            0.50           50081            0.50            9989            9934
challenging             18           90066            0.90            9934            0.10            9989            9934
difficult               20           91048            0.91            8952            0.09            9989            9934
impossible              30           99110            0.99             890            0.01            9989            9934
dyle@moghedien 10:10 ~/Source/dyle/death-of-krydort (main *)
```
Clearly the chances to drown are 50:50 on average. Any higher level is sure death.


Mode: *house1* with 1 luck:
``` 
$ python3 -m krydort --probes 100000 --mode house1 --luck 1 Athletics
Checking "Athletics" (DEX): attribute value = 6, skill value = 2
Game mode: house1 - LUCK spend: 1
DC-level           minimum        failures          f-rate         success          s-rate         fumbles        critical
easy                    10            9796            0.10           90204            0.90            4929           10191
average                 14           26427            0.26           73573            0.74            4929           10191
challenging             18           64746            0.65           35254            0.35            4929           10191
difficult               20           79912            0.80           20088            0.20            4929           10191
impossible              30           97965            0.98            2035            0.02            4929           10191
```
Here the chances of survival are greatly improved. On "challening" there is still a considerable chance of roughly 1/3
to stay on the living side. 


Mode: *house2* with 1 luck:
``` 
$ python3 -m krydort --probes 100000 --mode house2 --luck 1 Athletics
Checking "Athletics" (DEX): attribute value = 6, skill value = 2
Game mode: house2 - LUCK spend: 1
DC-level           minimum        failures          f-rate         success          s-rate         fumbles        critical
easy                    10             763            0.01           99237            0.99             763           10473
average                 14           33512            0.34           66488            0.66             763           10473
challenging             18           89527            0.90           10473            0.10             763           10473
difficult               20           89945            0.90           10055            0.10             763           10473
impossible              30           99628            1.00             372            0.00             763           10473
```
This is makes the success rate on easy and average dramatically higher compared to *normal*. Though to overcome
a rolling distance of 11 (e.g. challenging: 18 - attribute value = 6, skill value = 2 needs a roll of 11 to overcome)
is sure death.

Adding another initial D5 to the pool of dice in the first round, does make some difference:
```
$ python3 -m krydort --probes 100000 --mode house2 --luck 2 Athletics
Checking "Athletics" (DEX): attribute value = 6, skill value = 2
Game mode: house2 - LUCK spend: 2
DC-level           minimum        failures          f-rate         success          s-rate         fumbles        critical
easy                    10             172            0.00           99828            1.00             172           18320
average                 14           18737            0.19           81263            0.81             172           18320
challenging             18           81680            0.82           18320            0.18             172           18320
difficult               20           82461            0.82           17539            0.18             172           18320
impossible              30           99364            0.99             636            0.01             172           18320
``` 
Instead of dying at 90% now Krydort has a chance of 1 out of 5 to survive.

---

(C) Copyright 2020  
Oliver Maurhart, oliver.maurhart@headcode.space  
headcode.space e.U., https://www.headcode.space
