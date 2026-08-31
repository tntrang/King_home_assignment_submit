# Overview
Two tables are provided in the abtest database in Google BigQuery. 

## The assignment table 
It contains players assigned to the A/B test and attributes related to each player. Data from 2017/05/04 to 2017/05/22.
## The activity table 
It contains player activity for each day a player was active. Data from 2017/04/20 to 2017/05/22.

# Data schema

## The assignment table 
`king-ds-recruit-candidate-1114.abtest.assignment` 

| Field | Type | Mode | Description |
|-------|------|------|-------------|
| playerid | INTEGER | NULLABLE | Unique numeric identifier for each player |
| abtest_group | STRING | NULLABLE | The group the player was assigned to (A or B) |
| assignment_date | STRING | NULLABLE | The date when the player was assigned to the test |
| install_date | STRING | NULLABLE | The date when the player installed the game |
| conversion_date | STRING | NULLABLE | The date when the player made their first purchase |

## The activity table 
`king-ds-recruit-candidate-1114.abtest.activity` 

| Field | Type | Mode | Description |
|-------|------|------|-------------|
| playerid | INTEGER | NULLABLE | Unique numeric identifier for each player |
| activity_date | STRING | NULLABLE | The date of activity |
| purchases | INTEGER | NULLABLE | Number of purchases made this day |
| gameends | INTEGER | NULLABLE | Number of gamerounds played this day |
