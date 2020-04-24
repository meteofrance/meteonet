# Radar de Pluie

![Masks](../../img/Rain-Radar.png)

<a name="radar-data"></a>

## Données Radar

## Précipitations cumulées

![Masks](../../img/Rain-Radar-4.png)

## Code Qualité du Radar de Pluie

!!! info
    **Remark about the average quality code computation** : if there is no value for a whole day on 1 pixel, it will be indicated as a missing value in the `mean` file, else the mean computation is done over the non missing values for 1 day and 1 pixel.

![Masks](../../img/Rain-Radar-Quality-Code.png)

## Réfléctivité

$$ Z = 200.R^{1.6} \iff  R = (\frac{Z}{200})^\frac{1}{1.6}$$

!!! info
    The `200` and `1.6` coefficients depend on the type of rain and are specific to mainland France.

### Ancien Produit

!!! warning
    The old product data range from 01/01/2016 to 30/10/18 included. 


| Level | Reflectivity Range | Data value |
| ----- | ------------------ | ---------- |
| 0     | \(Z < 8\) dBZ      | 0          | 
| 1     | \(8 < Z < 16\) dBZ | 8          |
| 2     | \(16 < Z < 20\) dBZ| 16         |
| N     | \(17 + N < Z < 18 + N\) dBZ | \(17 + N\) |
| 53    | \(70 \leq Z\) dBZ | 70 |
| 255   | No value or missing data | 255 |


![Masks](../../img/Rain-Radar-Reflectivity-Old.png)

### Nouveau Produit

!!! warning
    The new product data range from 01/02/2018 to 31/12/18 included. 

![Masks](../../img/Rain-Radar-Reflectivity-New.png)
