|       | model            | engine   |   nrGPUs_a100 |   batchSize_a100 |   throughput_a100 |   throughput_tesla | errors_l_a100      | errors_l_tesla     |   Improvement |
|------:|:-----------------|:---------|--------------:|-----------------:|------------------:|-------------------:|:-------------------|:-------------------|--------------:|
| 59549 | Mixtral-8x7b     | autohf   |             1 |                8 |         0.189473  |          0.477247  | ok                 | ok                 |    -60.2987   |
| 59504 | Mixtral-8x7b     | autohf   |             1 |                4 |         0.117556  |          0.291902  | ok                 | ok                 |    -59.7278   |
| 59594 | Mixtral-8x7b     | autohf   |             1 |               16 |         0.341465  |          0.822023  | ok                 | ok                 |    -58.4603   |
| 59639 | Mixtral-8x7b     | autohf   |             1 |               32 |         0.613831  |          1.46952   | ok                 | ok                 |    -58.229    |
| 59414 | Mixtral-8x7b     | autohf   |             1 |                1 |         0.0416487 |          0.0972253 | ok                 | ok                 |    -57.1627   |
| 59459 | Mixtral-8x7b     | autohf   |             1 |                2 |         0.0811318 |          0.179028  | ok                 | ok                 |    -54.682    |
| 40830 | Gemma-7b         | autohf   |             2 |                2 |         1.70075   |          3.27523   | ok                 | ok                 |    -48.0723   |
| 40853 | Gemma-7b         | autohf   |             2 |                4 |         1.79874   |          3.40035   | ok                 | ok                 |    -47.1014   |
| 40807 | Gemma-7b         | autohf   |             2 |                1 |         1.64518   |          3.06567   | ok                 | ok                 |    -46.3354   |
| 40876 | Gemma-7b         | autohf   |             2 |                8 |         1.95706   |          3.44909   | ok                 | ok                 |    -43.2585   |
| 10032 | Starcoder2-3b    | autohf   |             8 |                8 |        72.1543    |         93.539     | ok                 | ok                 |    -22.8618   |
| 37993 | Gemma-2b         | autohf   |             2 |                4 |         4.18792   |          5.37646   | ok                 | ok                 |    -22.1063   |
| 38039 | Gemma-2b         | autohf   |             2 |               16 |         4.42687   |          5.5724    | ok                 | ok                 |    -20.5573   |
|  9987 | Starcoder2-3b    | autohf   |             8 |                4 |        46.7806    |         58.826     | ok                 | ok                 |    -20.4763   |
| 37970 | Gemma-2b         | autohf   |             2 |                2 |         4.07596   |          5.07908   | ok                 | ok                 |    -19.7499   |
| 37947 | Gemma-2b         | autohf   |             2 |                1 |         3.87647   |          4.78395   | ok                 | ok                 |    -18.9693   |
| 38062 | Gemma-2b         | autohf   |             2 |               32 |         4.56429   |          5.5566    | ok                 | CUDA out of memory |    -17.8582   |
| 38016 | Gemma-2b         | autohf   |             2 |                8 |         4.38399   |          5.24043   | ok                 | ok                 |    -16.343    |
| 50707 | Phi-2            | autohf   |             8 |                1 |        14.4057    |         16.7074    | ok                 | ok                 |    -13.7763   |
| 33957 | Codellama-7b-hf  | autohf   |             1 |                8 |        19.1648    |         22.1426    | ok                 | CUDA out of memory |    -13.4483   |
| 22704 | Bloom-7b1        | autohf   |             1 |                8 |        21.3648    |         24.4799    | ok                 | CUDA out of memory |    -12.7252   |
| 55924 | Mistral-7b       | autohf   |             1 |               16 |        17.8922    |         20.1609    | ok                 | CUDA out of memory |    -11.2533   |
| 12509 | Starcoder2-7b    | autohf   |             1 |               32 |        17.8973    |         20.0267    | ok                 | CUDA out of memory |    -10.6326   |
| 27116 | Codellama-13b-hf | autohf   |             2 |               16 |        11.3969    |         12.1326    | ok                 | CUDA out of memory |     -6.06365  |
| 57139 | Mistral-7b       | autohf   |             8 |                1 |        10.1214    |         10.6261    | ok                 | ok                 |     -4.74944  |
| 46835 | Phi-1_5          | autohf   |             8 |                1 |        27.7056    |         28.7635    | ok                 | ok                 |     -3.67776  |
| 50752 | Phi-2            | autohf   |             8 |                2 |        21.8267    |         22.2567    | ok                 | ok                 |     -1.93193  |
|  9942 | Starcoder2-3b    | autohf   |             8 |                2 |        35.2444    |         35.8171    | ok                 | ok                 |     -1.59885  |
| 16299 | Bloom-1b7        | autohf   |             4 |                1 |        24.3511    |         24.6436    | ok                 | ok                 |     -1.18682  |
| 13814 | Starcoder2-7b    | autohf   |             8 |                2 |        13.7522    |         13.8358    | ok                 | ok                 |     -0.604178 |
| 59909 | Mixtral-8x7b     | autohf   |             2 |                1 |         0.122569  |          0.123235  | ok                 | ok                 |     -0.54105  |
| 35352 | Codellama-7b-hf  | autohf   |             8 |                2 |        14.6838    |         14.717     | ok                 | ok                 |     -0.22593  |
| 23289 | Bloom-7b1        | autohf   |             2 |               32 |        23.5671    |         23.4117    | CUDA out of memory | CUDA out of memory |      0.663406 |
| 34542 | Codellama-7b-hf  | autohf   |             2 |               32 |        17.1055    |         16.9787    | ok                 | CUDA out of memory |      0.746621 |
| 50797 | Phi-2            | autohf   |             8 |                4 |        29.4564    |         29.1451    | ok                 | ok                 |      1.06808  |
| 24099 | Bloom-7b1        | autohf   |             8 |                2 |        16.1411    |         15.8461    | ok                 | ok                 |      1.86169  |
| 57181 | Mistral-7b       | autohf   |             8 |                2 |        14.0689    |         13.6647    | ok                 | ok                 |      2.95829  |
| 60089 | Mixtral-8x7b     | autohf   |             2 |               16 |         1.02021   |          0.985655  | CUDA out of memory | ok                 |      3.5061   |
| 16344 | Bloom-1b7        | autohf   |             4 |                2 |        39.1655    |         37.7448    | ok                 | ok                 |      3.76411  |
| 61169 | Mixtral-8x7b     | autohf   |             8 |               64 |        10.2525    |          9.86198   | ok                 | CUDA out of memory |      3.96006  |
| 46925 | Phi-1_5          | autohf   |             8 |                4 |        59.6026    |         56.8775    | ok                 | ok                 |      4.79124  |
| 46880 | Phi-1_5          | autohf   |             8 |                2 |        46.0882    |         43.7643    | ok                 | ok                 |      5.31003  |
| 60044 | Mixtral-8x7b     | autohf   |             2 |                8 |         0.605485  |          0.574737  | ok                 | ok                 |      5.34994  |
| 19687 | Bloom-3b         | autohf   |             4 |                1 |        19.425     |         18.3678    | ok                 | ok                 |      5.75534  |
| 24054 | Bloom-7b1        | autohf   |             8 |                1 |        12.5625    |         11.8741    | ok                 | ok                 |      5.79751  |
| 59999 | Mixtral-8x7b     | autohf   |             2 |                4 |         0.381535  |          0.359731  | ok                 | ok                 |      6.06121  |
| 35082 | Codellama-7b-hf  | autohf   |             4 |               64 |        17.2235    |         16.1679    | ok                 | CUDA out of memory |      6.52896  |
| 19957 | Bloom-3b         | autohf   |             4 |               64 |        37.2851    |         34.9918    | ok                 | CUDA out of memory |      6.55365  |
| 15804 | Bloom-1b7        | autohf   |             2 |                1 |        27.6831    |         25.9701    | ok                 | ok                 |      6.59595  |
| 33912 | Codellama-7b-hf  | autohf   |             1 |                4 |        19.0824    |         17.8689    | ok                 | CUDA out of memory |      6.79151  |
| 59954 | Mixtral-8x7b     | autohf   |             2 |                2 |         0.234303  |          0.218035  | ok                 | ok                 |      7.46122  |
|  1485 | Wizardcoder-15b  | autohf   |             8 |                1 |         6.22213   |          5.78207   | ok                 | ok                 |      7.61082  |
| 35397 | Codellama-7b-hf  | autohf   |             8 |                4 |        18.0635    |         16.7187    | ok                 | ok                 |      8.0438   |
| 16389 | Bloom-1b7        | autohf   |             4 |                4 |        53.9971    |         49.8964    | ok                 | ok                 |      8.21833  |
| 60989 | Mixtral-8x7b     | autohf   |             8 |                4 |         7.47065   |          6.88144   | ok                 | ok                 |      8.56236  |
| 17019 | Bloom-1b7        | autohf   |             8 |               32 |        70.2154    |         64.5828    | ok                 | CUDA out of memory |      8.72149  |
| 15534 | Bloom-1b7        | autohf   |             1 |               32 |        70.9355    |         64.968     | ok                 | CUDA out of memory |      9.18522  |
| 23559 | Bloom-7b1        | autohf   |             4 |                1 |        14.155     |         12.8871    | ok                 | ok                 |      9.83882  |
| 60944 | Mixtral-8x7b     | autohf   |             8 |                2 |         6.09434   |          5.53633   | ok                 | ok                 |     10.0791   |
| 24324 | Bloom-7b1        | autohf   |             8 |               64 |        18.6336    |         16.8972    | ok                 | CUDA out of memory |     10.2766   |
| 12464 | Starcoder2-7b    | autohf   |             1 |               16 |        19.4932    |         17.5968    | ok                 | CUDA out of memory |     10.7772   |
| 49492 | Phi-2            | autohf   |             1 |               64 |        25.0826    |         22.6348    | CUDA out of memory | CUDA out of memory |     10.814    |
|  9447 | Starcoder2-3b    | autohf   |             4 |                2 |        48.6102    |         43.8018    | ok                 | ok                 |     10.9777   |
| 27971 | Codellama-13b-hf | autohf   |             8 |                2 |        10.3243    |          9.28462   | ok                 | ok                 |     11.1978   |
| 55840 | Mistral-7b       | autohf   |             1 |                4 |        17.946     |         16.1028    | ok                 | ok                 |     11.4466   |
| 28061 | Codellama-13b-hf | autohf   |             8 |                8 |        11.4592    |         10.2819    | ok                 | ok                 |     11.4504   |
| 24189 | Bloom-7b1        | autohf   |             8 |                8 |        19.8843    |         17.8308    | ok                 | ok                 |     11.5162   |
| 13769 | Starcoder2-7b    | autohf   |             8 |                1 |        12.0027    |         10.753     | ok                 | ok                 |     11.6213   |
| 16794 | Bloom-1b7        | autohf   |             8 |                1 |        32.7793    |         29.3523    | ok                 | ok                 |     11.6752   |
| 23829 | Bloom-7b1        | autohf   |             4 |               64 |        21.4679    |         19.1893    | CUDA out of memory | CUDA out of memory |     11.8741   |
| 22659 | Bloom-7b1        | autohf   |             1 |                4 |        21.7721    |         19.4162    | ok                 | CUDA out of memory |     12.1337   |
|  1575 | Wizardcoder-15b  | autohf   |             8 |                4 |         7.04243   |          6.27455   | ok                 | ok                 |     12.238    |
| 24144 | Bloom-7b1        | autohf   |             8 |                4 |        20.1194    |         17.9209    | ok                 | ok                 |     12.2678   |
| 46970 | Phi-1_5          | autohf   |             8 |                8 |        66.6642    |         59.3358    | ok                 | ok                 |     12.3507   |
| 27071 | Codellama-13b-hf | autohf   |             2 |                8 |        11.6512    |         10.3646    | ok                 | ok                 |     12.4138   |
| 56719 | Mistral-7b       | autohf   |             4 |                2 |        15.9648    |         14.199     | ok                 | ok                 |     12.4359   |
| 28241 | Codellama-13b-hf | autohf   |             8 |              128 |         8.73104   |          7.75938   | ok                 | CUDA out of memory |     12.5223   |
| 61034 | Mixtral-8x7b     | autohf   |             8 |                8 |         9.05793   |          8.04921   | ok                 | ok                 |     12.532    |
| 28106 | Codellama-13b-hf | autohf   |             8 |               16 |        11.4893    |         10.2046    | ok                 | ok                 |     12.5893   |
| 28016 | Codellama-13b-hf | autohf   |             8 |                4 |        11.5632    |         10.2575    | ok                 | ok                 |     12.7298   |
| 13319 | Starcoder2-7b    | autohf   |             4 |                2 |        16.7201    |         14.8191    | ok                 | ok                 |     12.8285   |
| 35442 | Codellama-7b-hf  | autohf   |             8 |                8 |        18.5858    |         16.4723    | ok                 | ok                 |     12.8307   |
| 34497 | Codellama-7b-hf  | autohf   |             2 |               16 |        18.5049    |         16.3692    | ok                 | ok                 |     13.0469   |
| 57265 | Mistral-7b       | autohf   |             8 |                8 |        17.831     |         15.7679    | ok                 | ok                 |     13.0842   |
| 56386 | Mistral-7b       | autohf   |             2 |               16 |        17.5133    |         15.4782    | ok                 | ok                 |     13.1479   |
| 57223 | Mistral-7b       | autohf   |             8 |                4 |        17.8315    |         15.75      | ok                 | ok                 |     13.2164   |
| 55798 | Mistral-7b       | autohf   |             1 |                2 |        16.2824    |         14.3746    | ok                 | ok                 |     13.2725   |
| 32372 | Codellama-34b-hf | autohf   |             8 |                4 |         5.02724   |          4.43697   | ok                 | ok                 |     13.3036   |
| 35307 | Codellama-7b-hf  | autohf   |             8 |                1 |        13.2256    |         11.6589    | ok                 | ok                 |     13.4382   |
| 60899 | Mixtral-8x7b     | autohf   |             8 |                1 |         4.05066   |          3.56872   | ok                 | ok                 |     13.5044   |
| 56677 | Mistral-7b       | autohf   |             4 |                1 |        11.5928    |         10.2068    | ok                 | ok                 |     13.5791   |
| 23604 | Bloom-7b1        | autohf   |             4 |                2 |        18.3192    |         16.1218    | ok                 | ok                 |     13.6302   |
| 27026 | Codellama-13b-hf | autohf   |             2 |                4 |        11.76      |         10.3474    | ok                 | ok                 |     13.6517   |
| 56260 | Mistral-7b       | autohf   |             2 |                2 |        16.2145    |         14.2658    | ok                 | ok                 |     13.6603   |
| 55882 | Mistral-7b       | autohf   |             1 |                8 |        18.187     |         15.995     | ok                 | ok                 |     13.7037   |
| 56344 | Mistral-7b       | autohf   |             2 |                8 |        18.1771    |         15.9742    | ok                 | ok                 |     13.7902   |
| 27566 | Codellama-13b-hf | autohf   |             4 |                8 |        11.8278    |         10.3903    | ok                 | ok                 |     13.8342   |
| 30448 | Codellama-34b-hf | autohf   |             1 |                8 |         0.608048  |          0.533432  | ok                 | ok                 |     13.988    |
| 50212 | Phi-2            | autohf   |             4 |                1 |        19.5324    |         17.1313    | ok                 | ok                 |     14.016    |
| 34452 | Codellama-7b-hf  | autohf   |             2 |                8 |        19.0897    |         16.7323    | ok                 | ok                 |     14.0888   |
|  9897 | Starcoder2-3b    | autohf   |             8 |                1 |        21.9754    |         19.236     | ok                 | ok                 |     14.2411   |
| 13859 | Starcoder2-7b    | autohf   |             8 |                4 |        19.0904    |         16.6807    | ok                 | ok                 |     14.446    |
| 16434 | Bloom-1b7        | autohf   |             4 |                8 |        63.9115    |         55.8058    | ok                 | ok                 |     14.525    |
|  1620 | Wizardcoder-15b  | autohf   |             8 |                8 |         6.94179   |          6.05588   | ok                 | ok                 |     14.629    |
| 35487 | Codellama-7b-hf  | autohf   |             8 |               16 |        18.5815    |         16.1803    | ok                 | ok                 |     14.8404   |
| 34902 | Codellama-7b-hf  | autohf   |             4 |                4 |        19.3165    |         16.7933    | ok                 | ok                 |     15.0251   |
| 13904 | Starcoder2-7b    | autohf   |             8 |                8 |        19.3566    |         16.8259    | ok                 | ok                 |     15.0406   |
| 56302 | Mistral-7b       | autohf   |             2 |                4 |        17.976     |         15.6134    | ok                 | ok                 |     15.1316   |
| 46340 | Phi-1_5          | autohf   |             4 |                1 |        33.4966    |         29.0854    | ok                 | ok                 |     15.1663   |
| 30493 | Codellama-34b-hf | autohf   |             1 |               16 |         1.0967    |          0.952184  | ok                 | ok                 |     15.1768   |
| 34407 | Codellama-7b-hf  | autohf   |             2 |                4 |        18.8496    |         16.3616    | ok                 | ok                 |     15.2065   |
| 50842 | Phi-2            | autohf   |             8 |                8 |        36.0794    |         31.3078    | ok                 | ok                 |     15.2407   |
|  1530 | Wizardcoder-15b  | autohf   |             8 |                2 |         7.08136   |          6.1431    | ok                 | ok                 |     15.2734   |
| 33867 | Codellama-7b-hf  | autohf   |             1 |                2 |        17.4828    |         15.1653    | ok                 | ok                 |     15.2819   |
| 23694 | Bloom-7b1        | autohf   |             4 |                8 |        20.7603    |         18.0058    | ok                 | ok                 |     15.2975   |
| 57307 | Mistral-7b       | autohf   |             8 |               16 |        17.6727    |         15.3044    | ok                 | ok                 |     15.4747   |
| 23649 | Bloom-7b1        | autohf   |             4 |                4 |        20.85      |         18.0508    | ok                 | ok                 |     15.507    |
| 24234 | Bloom-7b1        | autohf   |             8 |               16 |        20.0805    |         17.3707    | ok                 | ok                 |     15.5994   |
| 61079 | Mixtral-8x7b     | autohf   |             8 |               16 |        10.2405    |          8.85667   | ok                 | ok                 |     15.6251   |
| 13274 | Starcoder2-7b    | autohf   |             4 |                1 |        13.1865    |         11.4006    | ok                 | ok                 |     15.6648   |
| 20407 | Bloom-3b         | autohf   |             8 |               32 |        50.0651    |         43.1911    | CUDA out of memory | CUDA out of memory |     15.9154   |
| 16884 | Bloom-1b7        | autohf   |             8 |                4 |        62.4171    |         53.7453    | ok                 | ok                 |     16.135    |
| 56428 | Mistral-7b       | autohf   |             2 |               32 |        16.6141    |         14.2957    | ok                 | ok                 |     16.2181   |
| 49987 | Phi-2            | autohf   |             2 |               64 |        40.4535    |         34.7139    | CUDA out of memory | CUDA out of memory |     16.5339   |
| 50527 | Phi-2            | autohf   |             4 |              128 |        34.0284    |         29.1381    | CUDA out of memory | CUDA out of memory |     16.7833   |
| 30403 | Codellama-34b-hf | autohf   |             1 |                4 |         0.332917  |          0.28489   | ok                 | ok                 |     16.8581   |
| 27611 | Codellama-13b-hf | autohf   |             4 |               16 |        11.9296    |         10.2026    | ok                 | ok                 |     16.9267   |
| 12914 | Starcoder2-7b    | autohf   |             2 |                8 |        19.8091    |         16.9292    | ok                 | ok                 |     17.0114   |
| 54669 | Codestral-22b    | autohf   |             8 |                4 |         7.01131   |          5.98725   | ok                 | ok                 |     17.104    |
| 18922 | Bloom-3b         | autohf   |             1 |               32 |        50.6081    |         43.198     | CUDA out of memory | CUDA out of memory |     17.154    |
| 30358 | Codellama-34b-hf | autohf   |             1 |                2 |         0.17181   |          0.146399  | ok                 | ok                 |     17.3572   |
| 32417 | Codellama-34b-hf | autohf   |             8 |                8 |         5.15458   |          4.38467   | ok                 | ok                 |     17.5591   |
| 34857 | Codellama-7b-hf  | autohf   |             4 |                2 |        16.9653    |         14.4301    | ok                 | ok                 |     17.5685   |
| 12374 | Starcoder2-7b    | autohf   |             1 |                4 |        20.1711    |         17.1503    | ok                 | ok                 |     17.6136   |
| 15579 | Bloom-1b7        | autohf   |             1 |               64 |        94.333     |         80.1942    | CUDA out of memory | CUDA out of memory |     17.6308   |
| 12419 | Starcoder2-7b    | autohf   |             1 |                8 |        19.778     |         16.8117    | ok                 | ok                 |     17.6443   |
| 19462 | Bloom-3b         | autohf   |             2 |               64 |        53.0974    |         45.1325    | CUDA out of memory | CUDA out of memory |     17.6477   |
| 54579 | Codestral-22b    | autohf   |             8 |                1 |         4.5491    |          3.86019   | ok                 | ok                 |     17.8465   |
| 23199 | Bloom-7b1        | autohf   |             2 |                8 |        21.281     |         18.0282    | ok                 | ok                 |     18.0427   |
| 27521 | Codellama-13b-hf | autohf   |             4 |                4 |        12.1263    |         10.2686    | ok                 | ok                 |     18.0911   |
| 23154 | Bloom-7b1        | autohf   |             2 |                4 |        21.5316    |         18.2157    | ok                 | ok                 |     18.2032   |
| 12869 | Starcoder2-7b    | autohf   |             2 |                4 |        20.258     |         17.1332    | ok                 | ok                 |     18.2378   |
| 34947 | Codellama-7b-hf  | autohf   |             4 |                8 |        19.8276    |         16.7644    | ok                 | ok                 |     18.2722   |
| 23739 | Bloom-7b1        | autohf   |             4 |               16 |        20.6858    |         17.4826    | ok                 | ok                 |     18.3222   |
| 16074 | Bloom-1b7        | autohf   |             2 |               64 |        82.0877    |         69.3182    | CUDA out of memory | CUDA out of memory |     18.4216   |
| 56761 | Mistral-7b       | autohf   |             4 |                4 |        19.0436    |         16.0733    | ok                 | ok                 |     18.4794   |
| 15849 | Bloom-1b7        | autohf   |             2 |                2 |        46.0146    |         38.8235    | ok                 | ok                 |     18.5226   |
| 27926 | Codellama-13b-hf | autohf   |             8 |                1 |         8.23814   |          6.95005   | ok                 | ok                 |     18.5336   |
| 34812 | Codellama-7b-hf  | autohf   |             4 |                1 |        13.8191    |         11.658     | ok                 | ok                 |     18.5377   |
| 47015 | Phi-1_5          | autohf   |             8 |               16 |        74.9455    |         63.2239    | ok                 | ok                 |     18.5399   |
| 46025 | Phi-1_5          | autohf   |             2 |               16 |        75.6219    |         63.7458    | ok                 | ok                 |     18.6305   |
| 49222 | Phi-2            | autohf   |             1 |                1 |        19.4578    |         16.3991    | ok                 | ok                 |     18.6519   |
| 17064 | Bloom-1b7        | autohf   |             8 |               64 |        94.5379    |         79.6759    | CUDA out of memory | CUDA out of memory |     18.6531   |
| 35532 | Codellama-7b-hf  | autohf   |             8 |               32 |        17.9848    |         15.157     | ok                 | ok                 |     18.6563   |
| 45935 | Phi-1_5          | autohf   |             2 |                4 |        67.5357    |         56.8996    | ok                 | ok                 |     18.6927   |
| 34362 | Codellama-7b-hf  | autohf   |             2 |                2 |        16.9991    |         14.3136    | ok                 | ok                 |     18.7625   |
| 19732 | Bloom-3b         | autohf   |             4 |                2 |        28.54      |         24.0115    | ok                 | ok                 |     18.8597   |
| 56803 | Mistral-7b       | autohf   |             4 |                8 |        18.9831    |         15.9698    | ok                 | ok                 |     18.8689   |
| 56845 | Mistral-7b       | autohf   |             4 |               16 |        18.4435    |         15.5137    | ok                 | ok                 |     18.8851   |
|  1125 | Wizardcoder-15b  | autohf   |             4 |                8 |         7.25378   |          6.0878    | ok                 | ok                 |     19.1528   |
| 12959 | Starcoder2-7b    | autohf   |             2 |               16 |        19.2896    |         16.1744    | ok                 | ok                 |     19.2596   |
| 50887 | Phi-2            | autohf   |             8 |               16 |        37.533     |         31.4659    | ok                 | ok                 |     19.2813   |
| 32552 | Codellama-34b-hf | autohf   |             8 |               64 |         4.10704   |          3.44056   | ok                 | ok                 |     19.3713   |
| 35037 | Codellama-7b-hf  | autohf   |             4 |               32 |        18.4407    |         15.413     | ok                 | ok                 |     19.6436   |
| 34992 | Codellama-7b-hf  | autohf   |             4 |               16 |        19.6471    |         16.4149    | ok                 | ok                 |     19.6905   |
| 49402 | Phi-2            | autohf   |             1 |               16 |        11.512     |          9.61534   | ok                 | ok                 |     19.725    |
| 32507 | Codellama-34b-hf | autohf   |             8 |               32 |         4.59153   |          3.83426   | ok                 | ok                 |     19.7499   |
| 23109 | Bloom-7b1        | autohf   |             2 |                2 |        19.7954    |         16.477     | ok                 | ok                 |     20.1396   |
| 28151 | Codellama-13b-hf | autohf   |             8 |               32 |        11.0267    |          9.17349   | ok                 | ok                 |     20.2023   |
| 20272 | Bloom-3b         | autohf   |             8 |                4 |        41.1596    |         34.241     | ok                 | ok                 |     20.2057   |
| 20182 | Bloom-3b         | autohf   |             8 |                1 |        25.3339    |         21.0748    | ok                 | ok                 |     20.2095   |
| 12824 | Starcoder2-7b    | autohf   |             2 |                2 |        18.0121    |         14.977     | ok                 | ok                 |     20.2648   |
| 13949 | Starcoder2-7b    | autohf   |             8 |               16 |        19.3667    |         16.1015    | ok                 | ok                 |     20.2787   |
| 57349 | Mistral-7b       | autohf   |             8 |               32 |        16.9768    |         14.1126    | ok                 | ok                 |     20.2953   |
| 49357 | Phi-2            | autohf   |             1 |                8 |         6.57839   |          5.46631   | ok                 | ok                 |     20.3443   |
| 26981 | Codellama-13b-hf | autohf   |             2 |                2 |        11.2769    |          9.36126   | ok                 | ok                 |     20.4634   |
| 23244 | Bloom-7b1        | autohf   |             2 |               16 |        21.036     |         17.4584    | ok                 | ok                 |     20.4922   |
| 12329 | Starcoder2-7b    | autohf   |             1 |                2 |        18.1927    |         15.0976    | ok                 | ok                 |     20.5008   |
| 54354 | Codestral-22b    | autohf   |             4 |               64 |         6.32655   |          5.23761   | ok                 | CUDA out of memory |     20.7909   |
| 54714 | Codestral-22b    | autohf   |             8 |                8 |         7.42334   |          6.14165   | ok                 | ok                 |     20.8687   |
| 56887 | Mistral-7b       | autohf   |             4 |               32 |        17.3395    |         14.3395    | ok                 | ok                 |     20.9209   |
| 16479 | Bloom-1b7        | autohf   |             4 |               16 |        67.258     |         55.5875    | ok                 | ok                 |     20.9947   |
| 46475 | Phi-1_5          | autohf   |             4 |                8 |        74.3417    |         61.3621    | ok                 | ok                 |     21.1525   |
| 56218 | Mistral-7b       | autohf   |             2 |                1 |        13.9508    |         11.5133    | ok                 | ok                 |     21.171    |
|  1170 | Wizardcoder-15b  | autohf   |             4 |               16 |         6.98897   |          5.76017   | ok                 | ok                 |     21.3327   |
|  1080 | Wizardcoder-15b  | autohf   |             4 |                4 |         7.70883   |          6.33793   | ok                 | ok                 |     21.6301   |
| 32327 | Codellama-34b-hf | autohf   |             8 |                2 |         4.61255   |          3.79061   | ok                 | ok                 |     21.6834   |
| 37763 | Gemma-2b         | autohf   |             1 |                8 |        45.8208    |         37.6364    | ok                 | ok                 |     21.7459   |
| 27656 | Codellama-13b-hf | autohf   |             4 |               32 |        11.2552    |          9.24354   | ok                 | ok                 |     21.7626   |
| 49447 | Phi-2            | autohf   |             1 |               32 |        16.7218    |         13.7301    | ok                 | ok                 |     21.7896   |
| 22614 | Bloom-7b1        | autohf   |             1 |                2 |        20.1132    |         16.5095    | ok                 | ok                 |     21.8278   |
| 13004 | Starcoder2-7b    | autohf   |             2 |               32 |        17.6622    |         14.493     | ok                 | ok                 |     21.8678   |
|  9492 | Starcoder2-3b    | autohf   |             4 |                4 |        72.8136    |         59.7266    | ok                 | ok                 |     21.9114   |
| 13409 | Starcoder2-7b    | autohf   |             4 |                8 |        20.6044    |         16.898     | ok                 | ok                 |     21.9341   |
| 15444 | Bloom-1b7        | autohf   |             1 |                8 |        71.5456    |         58.6665    | ok                 | ok                 |     21.9532   |
| 32462 | Codellama-34b-hf | autohf   |             8 |               16 |         5.1149    |          4.19095   | ok                 | ok                 |     22.0462   |
| 61124 | Mixtral-8x7b     | autohf   |             8 |               32 |        10.4402    |          8.54606   | ok                 | ok                 |     22.1637   |
|  1665 | Wizardcoder-15b  | autohf   |             8 |               16 |         7.01153   |          5.73534   | ok                 | ok                 |     22.2513   |
| 37740 | Gemma-2b         | autohf   |             1 |                4 |        44.0878    |         36.057     | ok                 | ok                 |     22.2726   |
| 45530 | Phi-1_5          | autohf   |             1 |               16 |        76.0558    |         62.1488    | ok                 | ok                 |     22.3768   |
| 20317 | Bloom-3b         | autohf   |             8 |                8 |        42.8325    |         34.9243    | ok                 | ok                 |     22.6438   |
| 19777 | Bloom-3b         | autohf   |             4 |                4 |        37.0609    |         30.215     | ok                 | ok                 |     22.6576   |
| 16929 | Bloom-1b7        | autohf   |             8 |                8 |        68.9924    |         56.2053    | ok                 | ok                 |     22.7507   |
| 19822 | Bloom-3b         | autohf   |             4 |                8 |        41.3995    |         33.704     | ok                 | ok                 |     22.8328   |
| 54894 | Codestral-22b    | autohf   |             8 |              128 |         5.41977   |          4.40595   | ok                 | CUDA out of memory |     23.0103   |
| 54624 | Codestral-22b    | autohf   |             8 |                2 |         6.47205   |          5.25534   | ok                 | ok                 |     23.1519   |
| 49762 | Phi-2            | autohf   |             2 |                2 |        31.2512    |         25.3179    | ok                 | ok                 |     23.4353   |
| 16974 | Bloom-1b7        | autohf   |             8 |               16 |        70.6364    |         57.1838    | ok                 | ok                 |     23.5251   |
| 45440 | Phi-1_5          | autohf   |             1 |                4 |        68.5939    |         55.528     | ok                 | ok                 |     23.5304   |
| 45485 | Phi-1_5          | autohf   |             1 |                8 |        75.4463    |         61.0657    | ok                 | ok                 |     23.5494   |
| 55756 | Mistral-7b       | autohf   |             1 |                1 |        14.2658    |         11.5384    | ok                 | ok                 |     23.6379   |
| 15984 | Bloom-1b7        | autohf   |             2 |               16 |        70.6848    |         57.1082    | ok                 | ok                 |     23.7734   |
| 35622 | Codellama-7b-hf  | autohf   |             8 |              128 |        14.5729    |         11.7547    | ok                 | CUDA out of memory |     23.9751   |
| 13364 | Starcoder2-7b    | autohf   |             4 |                4 |        20.9263    |         16.8741    | ok                 | ok                 |     24.0147   |
| 20227 | Bloom-3b         | autohf   |             8 |                2 |        35.291     |         28.4504    | ok                 | ok                 |     24.0438   |
| 24279 | Bloom-7b1        | autohf   |             8 |               32 |        19.7133    |         15.8855    | ok                 | ok                 |     24.0964   |
| 49267 | Phi-2            | autohf   |             1 |                2 |         1.97209   |          1.58905   | ok                 | ok                 |     24.1049   |
| 50257 | Phi-2            | autohf   |             4 |                2 |        27.2486    |         21.9457    | ok                 | ok                 |     24.1634   |
| 45980 | Phi-1_5          | autohf   |             2 |                8 |        74.7849    |         60.1704    | ok                 | ok                 |     24.2886   |
| 56470 | Mistral-7b       | autohf   |             2 |               64 |        15.5909    |         12.5432    | ok                 | ok                 |     24.2979   |
| 15939 | Bloom-1b7        | autohf   |             2 |                8 |        67.7409    |         54.4152    | ok                 | ok                 |     24.4887   |
|  1035 | Wizardcoder-15b  | autohf   |             4 |                2 |         7.89781   |          6.34265   | ok                 | ok                 |     24.5191   |
| 13454 | Starcoder2-7b    | autohf   |             4 |               16 |        20.1831    |         16.2066    | ok                 | ok                 |     24.5369   |
| 15354 | Bloom-1b7        | autohf   |             1 |                2 |        54.8134    |         43.9656    | ok                 | ok                 |     24.6732   |
| 16569 | Bloom-1b7        | autohf   |             4 |               64 |        62.0956    |         49.7789    | ok                 | CUDA out of memory |     24.7426   |
| 49852 | Phi-2            | autohf   |             2 |                8 |        41.8578    |         33.519     | ok                 | ok                 |     24.8779   |
| 15309 | Bloom-1b7        | autohf   |             1 |                1 |        37.6346    |         30.1314    | ok                 | ok                 |     24.9019   |
| 19867 | Bloom-3b         | autohf   |             4 |               16 |        42.662     |         34.1366    | ok                 | ok                 |     24.9744   |
| 35577 | Codellama-7b-hf  | autohf   |             8 |               64 |        16.9659    |         13.5747    | ok                 | ok                 |     24.9817   |
|  6599 | Starcoder-15b    | autohf   |             8 |                4 |        22.8024    |         18.24      | ok                 | ok                 |     25.0128   |
| 27476 | Codellama-13b-hf | autohf   |             4 |                2 |        11.6167    |          9.2879    | ok                 | ok                 |     25.0736   |
| 12779 | Starcoder2-7b    | autohf   |             2 |                1 |        15.4115    |         12.3153    | ok                 | ok                 |     25.1416   |
| 18697 | Bloom-3b         | autohf   |             1 |                1 |        27.3109    |         21.724     | ok                 | ok                 |     25.7175   |
| 23784 | Bloom-7b1        | autohf   |             4 |               32 |        20.0179    |         15.9173    | ok                 | ok                 |     25.7623   |
| 12284 | Starcoder2-7b    | autohf   |             1 |                1 |        15.658     |         12.4384    | ok                 | ok                 |     25.8842   |
| 45575 | Phi-1_5          | autohf   |             1 |               32 |        74.3725    |         59.0764    | ok                 | ok                 |     25.8922   |
| 46070 | Phi-1_5          | autohf   |             2 |               32 |        74.344     |         59.0474    | ok                 | ok                 |     25.9055   |
| 23064 | Bloom-7b1        | autohf   |             2 |                1 |        16.1772    |         12.8358    | ok                 | ok                 |     26.0319   |
| 50392 | Phi-2            | autohf   |             4 |               16 |        41.5697    |         32.9548    | ok                 | ok                 |     26.1417   |
| 15399 | Bloom-1b7        | autohf   |             1 |                4 |        66.2994    |         52.4258    | ok                 | ok                 |     26.4635   |
| 46430 | Phi-1_5          | autohf   |             4 |                4 |        65.4747    |         51.7686    | ok                 | ok                 |     26.4756   |
| 46520 | Phi-1_5          | autohf   |             4 |               16 |        78.3071    |         61.8876    | ok                 | ok                 |     26.5313   |
| 22569 | Bloom-7b1        | autohf   |             1 |                1 |        16.8418    |         13.271     | ok                 | ok                 |     26.9071   |
| 54219 | Codestral-22b    | autohf   |             4 |                8 |         7.86404   |          6.19473   | ok                 | ok                 |     26.9472   |
| 18742 | Bloom-3b         | autohf   |             1 |                2 |        36.9347    |         29.0777    | ok                 | ok                 |     27.0206   |
| 32282 | Codellama-34b-hf | autohf   |             8 |                1 |         3.70093   |          2.91216   | ok                 | ok                 |     27.0856   |
| 34317 | Codellama-7b-hf  | autohf   |             2 |                1 |        14.7629    |         11.6066    | ok                 | ok                 |     27.1944   |
| 15489 | Bloom-1b7        | autohf   |             1 |               16 |        73.6415    |         57.8633    | ok                 | ok                 |     27.268    |
| 50347 | Phi-2            | autohf   |             4 |                8 |        40.6772    |         31.9427    | ok                 | ok                 |     27.3442   |
| 19372 | Bloom-3b         | autohf   |             2 |               16 |        43.6387    |         34.2497    | ok                 | ok                 |     27.4134   |
| 16524 | Bloom-1b7        | autohf   |             4 |               32 |        67.4804    |         52.9218    | ok                 | ok                 |     27.5096   |
| 33822 | Codellama-7b-hf  | autohf   |             1 |                1 |        15.679     |         12.2948    | ok                 | ok                 |     27.5255   |
| 28196 | Codellama-13b-hf | autohf   |             8 |               64 |        10.663     |          8.35819   | ok                 | ok                 |     27.5748   |
| 57391 | Mistral-7b       | autohf   |             8 |               64 |        15.8746    |         12.4343    | ok                 | ok                 |     27.668    |
| 56929 | Mistral-7b       | autohf   |             4 |               64 |        16.1238    |         12.6187    | ok                 | ok                 |     27.777    |
| 15894 | Bloom-1b7        | autohf   |             2 |                4 |        60.5329    |         47.3195    | ok                 | ok                 |     27.9237   |
| 47060 | Phi-1_5          | autohf   |             8 |               32 |        75.3742    |         58.8522    | ok                 | ok                 |     28.0737   |
| 19237 | Bloom-3b         | autohf   |             2 |                2 |        33.3372    |         25.999     | ok                 | ok                 |     28.225    |
| 18787 | Bloom-3b         | autohf   |             1 |                4 |        43.0657    |         33.5846    | ok                 | ok                 |     28.2305   |
| 49312 | Phi-2            | autohf   |             1 |                4 |         3.96835   |          3.08937   | ok                 | ok                 |     28.4518   |
| 19912 | Bloom-3b         | autohf   |             4 |               32 |        41.0307    |         31.9308    | ok                 | ok                 |     28.4988   |
| 50932 | Phi-2            | autohf   |             8 |               32 |        38.4097    |         29.8865    | ok                 | ok                 |     28.5184   |
| 16839 | Bloom-1b7        | autohf   |             8 |                2 |        51.4836    |         40.0588    | ok                 | ok                 |     28.5203   |
| 18832 | Bloom-3b         | autohf   |             1 |                8 |        44.5925    |         34.5869    | ok                 | ok                 |     28.9288   |
| 19327 | Bloom-3b         | autohf   |             2 |                8 |        43.5145    |         33.6872    | ok                 | ok                 |     29.1724   |
|   540 | Wizardcoder-15b  | autohf   |             2 |                2 |         8.06009   |          6.2388    | ok                 | ok                 |     29.193    |
| 19192 | Bloom-3b         | autohf   |             2 |                1 |        22.0539    |         17.0577    | ok                 | ok                 |     29.29     |
| 45350 | Phi-1_5          | autohf   |             1 |                1 |        37.0227    |         28.6259    | ok                 | ok                 |     29.3328   |
| 19417 | Bloom-3b         | autohf   |             2 |               32 |        42.4163    |         32.7951    | ok                 | CUDA out of memory |     29.3374   |
| 56971 | Mistral-7b       | autohf   |             4 |              128 |        13.9042    |         10.7485    | ok                 | CUDA out of memory |     29.3593   |
| 13049 | Starcoder2-7b    | autohf   |             2 |               64 |        16.444     |         12.7034    | ok                 | ok                 |     29.445    |
| 13994 | Starcoder2-7b    | autohf   |             8 |               32 |        18.6978    |         14.4438    | ok                 | ok                 |     29.4524   |
| 20362 | Bloom-3b         | autohf   |             8 |               16 |        44.3084    |         34.1763    | ok                 | ok                 |     29.6465   |
| 37786 | Gemma-2b         | autohf   |             1 |               16 |        44.4828    |         34.3019    | ok                 | ok                 |     29.6803   |
| 51022 | Phi-2            | autohf   |             8 |              128 |        31.5728    |         24.3198    | ok                 | CUDA out of memory |     29.8235   |
| 50437 | Phi-2            | autohf   |             4 |               32 |        40.561     |         31.2347    | ok                 | ok                 |     29.8588   |
| 54804 | Codestral-22b    | autohf   |             8 |               32 |         6.76839   |          5.20928   | ok                 | ok                 |     29.9296   |
| 30313 | Codellama-34b-hf | autohf   |             1 |                1 |         0.0873788 |          0.0672262 | ok                 | ok                 |     29.9774   |
| 57433 | Mistral-7b       | autohf   |             8 |              128 |        13.7627    |         10.5882    | ok                 | ok                 |     29.9821   |
| 46565 | Phi-1_5          | autohf   |             4 |               32 |        77.2616    |         59.2733    | ok                 | ok                 |     30.348    |
| 54309 | Codestral-22b    | autohf   |             4 |               32 |         6.85707   |          5.25837   | ok                 | ok                 |     30.4029   |
| 19282 | Bloom-3b         | autohf   |             2 |                4 |        40.4633    |         31.0232    | ok                 | ok                 |     30.4292   |
| 49807 | Phi-2            | autohf   |             2 |                4 |        38.8558    |         29.7599    | ok                 | ok                 |     30.5642   |
| 37694 | Gemma-2b         | autohf   |             1 |                1 |        28.7912    |         22.0444    | ok                 | ok                 |     30.6054   |
| 49717 | Phi-2            | autohf   |             2 |                1 |        21.9965    |         16.838     | ok                 | ok                 |     30.636    |
| 50302 | Phi-2            | autohf   |             4 |                4 |        37.2093    |         28.4639    | ok                 | ok                 |     30.7246   |
|   990 | Wizardcoder-15b  | autohf   |             4 |                1 |         7.59942   |          5.81213   | ok                 | ok                 |     30.751    |
| 16029 | Bloom-1b7        | autohf   |             2 |               32 |        69.7004    |         53.2867    | ok                 | ok                 |     30.8028   |
| 54174 | Codestral-22b    | autohf   |             4 |                4 |         7.88142   |          6.0072    | ok                 | ok                 |     31.1997   |
| 49897 | Phi-2            | autohf   |             2 |               16 |        43.225     |         32.8687    | ok                 | ok                 |     31.5082   |
| 27431 | Codellama-13b-hf | autohf   |             4 |                1 |         9.35386   |          7.09674   | ok                 | ok                 |     31.805    |
|  9537 | Starcoder2-3b    | autohf   |             4 |                8 |       118.126     |         89.5785    | ok                 | ok                 |     31.8684   |
| 13499 | Starcoder2-7b    | autohf   |             4 |               32 |        19.1829    |         14.5264    | ok                 | ok                 |     32.0556   |
| 54759 | Codestral-22b    | autohf   |             8 |               16 |         7.71151   |          5.83708   | ok                 | ok                 |     32.1124   |
| 18877 | Bloom-3b         | autohf   |             1 |               16 |        45.2595    |         34.2498    | ok                 | ok                 |     32.1454   |
| 37717 | Gemma-2b         | autohf   |             1 |                2 |        37.4063    |         28.3005    | ok                 | ok                 |     32.1753   |
| 10077 | Starcoder2-3b    | autohf   |             8 |               16 |       150.591     |        113.77      | ok                 | ok                 |     32.3643   |
|  6554 | Starcoder-15b    | autohf   |             8 |                2 |        18.9913    |         14.3369    | ok                 | ok                 |     32.4644   |
|  1800 | Wizardcoder-15b  | autohf   |             8 |              128 |         5.1327    |          3.86829   | ok                 | CUDA out of memory |     32.6865   |
| 54129 | Codestral-22b    | autohf   |             4 |                2 |         7.02851   |          5.29264   | ok                 | ok                 |     32.7977   |
| 46385 | Phi-1_5          | autohf   |             4 |                2 |        51.265     |         38.3298    | ok                 | ok                 |     33.7472   |
| 13094 | Starcoder2-7b    | autohf   |             2 |              128 |        16.2301    |         12.1085    | CUDA out of memory | CUDA out of memory |     34.0396   |
|  8907 | Starcoder2-3b    | autohf   |             2 |                1 |        33.3936    |         24.8853    | ok                 | ok                 |     34.1899   |
| 46115 | Phi-1_5          | autohf   |             2 |               64 |        86.0217    |         64.0318    | CUDA out of memory | CUDA out of memory |     34.3422   |
| 54264 | Codestral-22b    | autohf   |             4 |               16 |         7.90605   |          5.87419   | ok                 | ok                 |     34.5895   |
| 45620 | Phi-1_5          | autohf   |             1 |               64 |        86.0469    |         63.9084    | CUDA out of memory | CUDA out of memory |     34.6411   |
| 50482 | Phi-2            | autohf   |             4 |               64 |        37.1905    |         27.579     | ok                 | ok                 |     34.8505   |
| 49942 | Phi-2            | autohf   |             2 |               32 |        41.9604    |         30.9046    | ok                 | ok                 |     35.7738   |
| 50977 | Phi-2            | autohf   |             8 |               64 |        35.9846    |         26.4962    | ok                 | ok                 |     35.8103   |
| 45890 | Phi-1_5          | autohf   |             2 |                2 |        53.353     |         39.2638    | ok                 | ok                 |     35.8833   |
|   495 | Wizardcoder-15b  | autohf   |             2 |                1 |         7.99194   |          5.85329   | ok                 | ok                 |     36.5375   |
| 54084 | Codestral-22b    | autohf   |             4 |                1 |         5.39665   |          3.94839   | ok                 | ok                 |     36.6798   |
| 47105 | Phi-1_5          | autohf   |             8 |               64 |        87.826     |         63.9775    | CUDA out of memory | CUDA out of memory |     37.2764   |
|  1710 | Wizardcoder-15b  | autohf   |             8 |               32 |         6.47802   |          4.717     | ok                 | ok                 |     37.3333   |
|  1260 | Wizardcoder-15b  | autohf   |             4 |               64 |         6.24216   |          4.53129   | ok                 | CUDA out of memory |     37.7568   |
| 26936 | Codellama-13b-hf | autohf   |             2 |                1 |         9.69853   |          7.01307   | ok                 | ok                 |     38.2923   |
| 14039 | Starcoder2-7b    | autohf   |             8 |               64 |        17.6549    |         12.6789    | ok                 | ok                 |     39.2465   |
|  1215 | Wizardcoder-15b  | autohf   |             4 |               32 |         6.59429   |          4.73113   | ok                 | ok                 |     39.3808   |
| 45395 | Phi-1_5          | autohf   |             1 |                2 |        54.2758    |         38.92      | ok                 | ok                 |     39.4545   |
|  9402 | Starcoder2-3b    | autohf   |             4 |                1 |        29.0505    |         20.7724    | ok                 | ok                 |     39.8513   |
| 13544 | Starcoder2-7b    | autohf   |             4 |               64 |        17.8903    |         12.7328    | ok                 | ok                 |     40.5048   |
|  6644 | Starcoder-15b    | autohf   |             8 |                8 |        30.4346    |         21.5151    | ok                 | ok                 |     41.4571   |
| 53274 | Codestral-22b    | autohf   |             1 |               16 |         2.20325   |          1.55019   | CUDA out of memory | CUDA out of memory |     42.1278   |
| 46610 | Phi-1_5          | autohf   |             4 |               64 |        91.1395    |         63.9707    | CUDA out of memory | CUDA out of memory |     42.4708   |
|  6509 | Starcoder-15b    | autohf   |             8 |                1 |        16.6364    |         11.6132    | ok                 | ok                 |     43.254    |
| 54849 | Codestral-22b    | autohf   |             8 |               64 |         6.26542   |          4.33774   | ok                 | ok                 |     44.4399   |
| 14084 | Starcoder2-7b    | autohf   |             8 |              128 |        15.2763    |         10.5485    | ok                 | ok                 |     44.8197   |
| 13589 | Starcoder2-7b    | autohf   |             4 |              128 |        15.4129    |         10.6009    | ok                 | ok                 |     45.3932   |
| 53229 | Codestral-22b    | autohf   |             1 |                8 |         1.30809   |          0.897199  | ok                 | ok                 |     45.7966   |
| 45845 | Phi-1_5          | autohf   |             2 |                1 |        36.2123    |         24.6222    | ok                 | ok                 |     47.0716   |
|  9042 | Starcoder2-3b    | autohf   |             2 |                8 |       149.479     |        101.104     | ok                 | ok                 |     47.8465   |
|  8997 | Starcoder2-3b    | autohf   |             2 |                4 |        91.961     |         61.5138    | ok                 | ok                 |     49.4966   |
|   135 | Wizardcoder-15b  | autohf   |             1 |                8 |         1.53779   |          1.02574   | ok                 | ok                 |     49.9201   |
|  6059 | Starcoder-15b    | autohf   |             4 |                2 |        23.3648    |         15.3574    | ok                 | ok                 |     52.1402   |
|  8952 | Starcoder2-3b    | autohf   |             2 |                2 |        56.4728    |         36.9559    | ok                 | ok                 |     52.8111   |
|  6104 | Starcoder-15b    | autohf   |             4 |                4 |        29.6493    |         19.2429    | ok                 | ok                 |     54.0792   |
|  1755 | Wizardcoder-15b  | autohf   |             8 |               64 |         6.18935   |          4.01456   | ok                 | ok                 |     54.1728   |
|  8412 | Starcoder2-3b    | autohf   |             1 |                1 |        44.799     |         28.9728    | ok                 | ok                 |     54.6243   |
| 53094 | Codestral-22b    | autohf   |             1 |                1 |         0.171607  |          0.110509  | ok                 | ok                 |     55.2875   |
|     0 | Wizardcoder-15b  | autohf   |             1 |                1 |         0.347988  |          0.220719  | ok                 | ok                 |     57.6608   |
| 53184 | Codestral-22b    | autohf   |             1 |                4 |         0.726809  |          0.458258  | ok                 | ok                 |     58.6026   |
| 53139 | Codestral-22b    | autohf   |             1 |                2 |         0.397589  |          0.248307  | ok                 | ok                 |     60.1199   |
|    45 | Wizardcoder-15b  | autohf   |             1 |                2 |         0.536535  |          0.334842  | ok                 | ok                 |     60.2352   |
|    90 | Wizardcoder-15b  | autohf   |             1 |                4 |         0.925005  |          0.577069  | ok                 | ok                 |     60.2937   |
| 10122 | Starcoder2-3b    | autohf   |             8 |               32 |       203.446     |        126.173     | ok                 | ok                 |     61.2433   |
|  8457 | Starcoder2-3b    | autohf   |             1 |                2 |        79.7182    |         49.2955    | ok                 | ok                 |     61.7149   |
| 40600 | Gemma-7b         | autohf   |             1 |                4 |         5.44832   |          3.29947   | ok                 | CUDA out of memory |     65.1274   |
|  9582 | Starcoder2-3b    | autohf   |             4 |               16 |       204.339     |        123.03      | ok                 | ok                 |     66.0886   |
|  3388 | Wizardcoder-33b  | autohf   |             1 |                1 |         0.099672  |          0.0591564 | ok                 | ok                 |     68.489    |
|  5564 | Starcoder-15b    | autohf   |             2 |                2 |        26.7208    |         15.7702    | ok                 | ok                 |     69.4383   |
|  8547 | Starcoder2-3b    | autohf   |             1 |                8 |       191.476     |        110.875     | ok                 | ok                 |     72.6954   |
| 40554 | Gemma-7b         | autohf   |             1 |                1 |         2.06862   |          1.19167   | ok                 | ok                 |     73.5892   |
|  6014 | Starcoder-15b    | autohf   |             4 |                1 |        19.9117    |         11.4397    | ok                 | ok                 |     74.0581   |
|  5519 | Starcoder-15b    | autohf   |             2 |                1 |        21.4178    |         12.1886    | ok                 | ok                 |     75.7193   |
| 40577 | Gemma-7b         | autohf   |             1 |                2 |         3.63156   |          2.04033   | ok                 | ok                 |     77.9887   |
|  8502 | Starcoder2-3b    | autohf   |             1 |                4 |       130.115     |         72.5231    | ok                 | ok                 |     79.4117   |
|  6149 | Starcoder-15b    | autohf   |             4 |                8 |        39.389     |         21.8567    | ok                 | ok                 |     80.2144   |
|  5609 | Starcoder-15b    | autohf   |             2 |                4 |        35.6733    |         19.6113    | ok                 | ok                 |     81.9018   |
|  9087 | Starcoder2-3b    | autohf   |             2 |               16 |       241.766     |        128.14      | ok                 | ok                 |     88.6738   |
|  9627 | Starcoder2-3b    | autohf   |             4 |               32 |       247.92      |        129.559     | ok                 | ok                 |     91.3566   |
|  6689 | Starcoder-15b    | autohf   |             8 |               16 |        41.6689    |         21.7275    | ok                 | ok                 |     91.7796   |
| 26531 | Codellama-13b-hf | autohf   |             1 |                4 |         2.3381    |          1.21775   | ok                 | CUDA out of memory |     92.0012   |
| 10167 | Starcoder2-3b    | autohf   |             8 |               64 |       228.978     |        118.772     | ok                 | ok                 |     92.7884   |
| 10257 | Starcoder2-3b    | autohf   |             8 |              256 |       218.971     |        111.898     | CUDA out of memory | CUDA out of memory |     95.6871   |
| 26486 | Codellama-13b-hf | autohf   |             1 |                2 |         1.28913   |          0.649235  | ok                 | ok                 |     98.5612   |
|  5654 | Starcoder-15b    | autohf   |             2 |                8 |        43.8247    |         21.9869    | ok                 | ok                 |     99.3213   |
|  9132 | Starcoder2-3b    | autohf   |             2 |               32 |       262.587     |        130.404     | ok                 | ok                 |    101.364    |
| 33562 | Codellama-70b-hf | autohf   |             8 |               16 |         2.85048   |          1.41123   | ok                 | ok                 |    101.985    |
|  8592 | Starcoder2-3b    | autohf   |             1 |               16 |       262.801     |        128.958     | ok                 | ok                 |    103.788    |
| 33263 | Codellama-70b-hf | autohf   |             4 |                4 |         0.385787  |          0.186822  | CUDA out of memory | ok                 |    106.499    |
| 26441 | Codellama-13b-hf | autohf   |             1 |                1 |         0.701012  |          0.3373    | ok                 | ok                 |    107.831    |
|  9672 | Starcoder2-3b    | autohf   |             4 |               64 |       253.587     |        120.872     | ok                 | ok                 |    109.798    |
|  8637 | Starcoder2-3b    | autohf   |             1 |               32 |       282.427     |        134.501     | ok                 | ok                 |    109.981    |
|  9177 | Starcoder2-3b    | autohf   |             2 |               64 |       259.242     |        123.138     | ok                 | ok                 |    110.53     |
| 33240 | Codellama-70b-hf | autohf   |             4 |                2 |         0.204748  |          0.0971807 | ok                 | ok                 |    110.687    |
|  8682 | Starcoder2-3b    | autohf   |             1 |               64 |       264.37      |        124.69      | ok                 | ok                 |    112.021    |
|  6194 | Starcoder-15b    | autohf   |             4 |               16 |        48.4936    |         21.6823    | ok                 | ok                 |    123.655    |
| 10212 | Starcoder2-3b    | autohf   |             8 |              128 |       222.811     |         98.9499    | ok                 | ok                 |    125.175    |
|  5699 | Starcoder-15b    | autohf   |             2 |               16 |        50.2131    |         22.1368    | ok                 | ok                 |    126.831    |
| 33217 | Codellama-70b-hf | autohf   |             4 |                1 |         0.100732  |          0.0437865 | ok                 | ok                 |    130.052    |
|  8727 | Starcoder2-3b    | autohf   |             1 |              128 |       250.552     |        106.149     | ok                 | ok                 |    136.038    |
|  9717 | Starcoder2-3b    | autohf   |             4 |              128 |       238.621     |        100.909     | ok                 | ok                 |    136.471    |
|  9222 | Starcoder2-3b    | autohf   |             2 |              128 |       248.162     |        103.989     | ok                 | ok                 |    138.642    |
|  6734 | Starcoder-15b    | autohf   |             8 |               32 |        42.9915    |         17.8179    | ok                 | ok                 |    141.283    |
|  9762 | Starcoder2-3b    | autohf   |             4 |              256 |       278.266     |        115.156     | CUDA out of memory | CUDA out of memory |    141.644    |
|  5744 | Starcoder-15b    | autohf   |             2 |               32 |        47.8857    |         18.6014    | ok                 | ok                 |    157.431    |
|  6239 | Starcoder-15b    | autohf   |             4 |               32 |        46.4632    |         17.9967    | ok                 | ok                 |    158.177    |
| 33539 | Codellama-70b-hf | autohf   |             8 |                8 |         2.97122   |          1.07638   | ok                 | ok                 |    176.037    |
| 53634 | Codestral-22b    | autohf   |             2 |                2 |         1.63159   |          0.554558  | ok                 | CUDA out of memory |    194.215    |
| 60584 | Mixtral-8x7b     | autohf   |             4 |               16 |         4.86339   |          1.6441    | CUDA out of memory | ok                 |    195.809    |
|  6869 | Starcoder-15b    | autohf   |             8 |              256 |        37.1036    |         12.3236    | CUDA out of memory | CUDA out of memory |    201.076    |
|  5204 | Starcoder-15b    | autohf   |             1 |               16 |        55.1121    |         18.1792    | ok                 | CUDA out of memory |    203.16     |
|  5789 | Starcoder-15b    | autohf   |             2 |               64 |        46.2125    |         15.1022    | ok                 | CUDA out of memory |    205.998    |
|  6779 | Starcoder-15b    | autohf   |             8 |               64 |        42.9577    |         13.9679    | ok                 | ok                 |    207.546    |
| 53589 | Codestral-22b    | autohf   |             2 |                1 |         0.830832  |          0.269382  | ok                 | ok                 |    208.422    |
| 60404 | Mixtral-8x7b     | autohf   |             4 |                1 |         0.718812  |          0.230167  | ok                 | ok                 |    212.3      |
| 60539 | Mixtral-8x7b     | autohf   |             4 |                8 |         3.1633    |          1.01213   | ok                 | ok                 |    212.54     |
|  6284 | Starcoder-15b    | autohf   |             4 |               64 |        44.8776    |         13.9874    | ok                 | ok                 |    220.843    |
|  6824 | Starcoder-15b    | autohf   |             8 |              128 |        38.5438    |         11.9078    | ok                 | ok                 |    223.686    |
|  6329 | Starcoder-15b    | autohf   |             4 |              128 |        39.2828    |         11.9642    | ok                 | ok                 |    228.336    |
| 60494 | Mixtral-8x7b     | autohf   |             4 |                4 |         1.99012   |          0.601964  | ok                 | ok                 |    230.605    |
| 60449 | Mixtral-8x7b     | autohf   |             4 |                2 |         1.29227   |          0.384971  | ok                 | ok                 |    235.68     |
| 31832 | Codellama-34b-hf | autohf   |             4 |                2 |         4.91377   |          1.4593    | ok                 | CUDA out of memory |    236.72     |
| 33516 | Codellama-70b-hf | autohf   |             8 |                4 |         2.90329   |          0.6633    | ok                 | ok                 |    337.705    |
|  5159 | Starcoder-15b    | autohf   |             1 |                8 |        52.7195    |         11.9437    | ok                 | ok                 |    341.401    |
| 31787 | Codellama-34b-hf | autohf   |             4 |                1 |         4.12485   |          0.828773  | ok                 | ok                 |    397.706    |
|  5114 | Starcoder-15b    | autohf   |             1 |                4 |        46.5492    |          8.18198   | ok                 | ok                 |    468.923    |
| 33493 | Codellama-70b-hf | autohf   |             8 |                2 |         2.35124   |          0.395156  | ok                 | ok                 |    495.016    |
|  5069 | Starcoder-15b    | autohf   |             1 |                2 |        37.9743    |          5.13317   | ok                 | ok                 |    639.782    |
| 33470 | Codellama-70b-hf | autohf   |             8 |                1 |         1.79016   |          0.210669  | ok                 | ok                 |    749.751    |
|  5024 | Starcoder-15b    | autohf   |             1 |                1 |        30.6823    |          3.51044   | ok                 | ok                 |    774.028    |
|  4067 | Wizardcoder-33b  | autohf   |             4 |                2 |         1.64168   |          0.148876  | ok                 | ok                 |   1002.72     |
|   180 | Wizardcoder-15b  | autohf   |             1 |               16 |         2.59407   |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|   225 | Wizardcoder-15b  | autohf   |             1 |               32 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|   270 | Wizardcoder-15b  | autohf   |             1 |               64 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|   315 | Wizardcoder-15b  | autohf   |             1 |              128 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|   360 | Wizardcoder-15b  | autohf   |             1 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|   405 | Wizardcoder-15b  | autohf   |             1 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|   450 | Wizardcoder-15b  | autohf   |             1 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|   585 | Wizardcoder-15b  | autohf   |             2 |                4 |       nan         |          6.32861   | CUDA out of memory | ok                 |    nan        |
|   630 | Wizardcoder-15b  | autohf   |             2 |                8 |       nan         |          6.64159   | CUDA out of memory | CUDA out of memory |    nan        |
|   675 | Wizardcoder-15b  | autohf   |             2 |               16 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|   720 | Wizardcoder-15b  | autohf   |             2 |               32 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|   765 | Wizardcoder-15b  | autohf   |             2 |               64 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|   810 | Wizardcoder-15b  | autohf   |             2 |              128 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|   855 | Wizardcoder-15b  | autohf   |             2 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|   900 | Wizardcoder-15b  | autohf   |             2 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|   945 | Wizardcoder-15b  | autohf   |             2 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|  1305 | Wizardcoder-15b  | autohf   |             4 |              128 |         6.13912   |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|  1350 | Wizardcoder-15b  | autohf   |             4 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|  1395 | Wizardcoder-15b  | autohf   |             4 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|  1440 | Wizardcoder-15b  | autohf   |             4 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|  1845 | Wizardcoder-15b  | autohf   |             8 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|  1890 | Wizardcoder-15b  | autohf   |             8 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|  1935 | Wizardcoder-15b  | autohf   |             8 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|  3418 | Wizardcoder-33b  | autohf   |             1 |                2 |       nan         |          0.11452   | CUDA out of memory | ok                 |    nan        |
|  3709 | Wizardcoder-33b  | autohf   |             2 |                1 |       nan         |        nan         | CUDA error         | CUDA out of memory |    nan        |
|  3739 | Wizardcoder-33b  | autohf   |             2 |                2 |       nan         |          0.129792  | CUDA out of memory | ok                 |    nan        |
|  3769 | Wizardcoder-33b  | autohf   |             2 |                4 |       nan         |          0.210122  | CUDA out of memory | ok                 |    nan        |
|  3799 | Wizardcoder-33b  | autohf   |             2 |                8 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|  3829 | Wizardcoder-33b  | autohf   |             2 |               16 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|  3859 | Wizardcoder-33b  | autohf   |             2 |               32 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|  3889 | Wizardcoder-33b  | autohf   |             2 |               64 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|  3919 | Wizardcoder-33b  | autohf   |             2 |              128 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|  3949 | Wizardcoder-33b  | autohf   |             2 |              256 |       nan         |        nan         | CUDA out of memory | killed-noInfo      |    nan        |
|  4037 | Wizardcoder-33b  | autohf   |             4 |                1 |         1.63223   |        nan         | ok                 | CUDA out of memory |    nan        |
|  4097 | Wizardcoder-33b  | autohf   |             4 |                4 |       nan         |          0.232419  | CUDA out of memory | ok                 |    nan        |
|  4127 | Wizardcoder-33b  | autohf   |             4 |                8 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|  4157 | Wizardcoder-33b  | autohf   |             4 |               16 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|  4187 | Wizardcoder-33b  | autohf   |             4 |               32 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|  4217 | Wizardcoder-33b  | autohf   |             4 |               64 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|  4247 | Wizardcoder-33b  | autohf   |             4 |              128 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|  4277 | Wizardcoder-33b  | autohf   |             4 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|  4336 | Wizardcoder-33b  | autohf   |             8 |                1 |       nan         |          0.250903  | CUDA out of memory | ok                 |    nan        |
|  4366 | Wizardcoder-33b  | autohf   |             8 |                2 |       nan         |          0.232476  | CUDA out of memory | ok                 |    nan        |
|  4396 | Wizardcoder-33b  | autohf   |             8 |                4 |       nan         |          0.222067  | CUDA out of memory | ok                 |    nan        |
|  4426 | Wizardcoder-33b  | autohf   |             8 |                8 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|  4456 | Wizardcoder-33b  | autohf   |             8 |               16 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|  4486 | Wizardcoder-33b  | autohf   |             8 |               32 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|  4516 | Wizardcoder-33b  | autohf   |             8 |               64 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|  4546 | Wizardcoder-33b  | autohf   |             8 |              128 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|  4576 | Wizardcoder-33b  | autohf   |             8 |              256 |       nan         |        nan         | CUDA out of memory | killed-noInfo      |    nan        |
|  5249 | Starcoder-15b    | autohf   |             1 |               32 |        62.4213    |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|  5294 | Starcoder-15b    | autohf   |             1 |               64 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|  5339 | Starcoder-15b    | autohf   |             1 |              128 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|  5384 | Starcoder-15b    | autohf   |             1 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|  5429 | Starcoder-15b    | autohf   |             1 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|  5474 | Starcoder-15b    | autohf   |             1 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|  5834 | Starcoder-15b    | autohf   |             2 |              128 |        50.2937    |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|  5879 | Starcoder-15b    | autohf   |             2 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|  5924 | Starcoder-15b    | autohf   |             2 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|  5969 | Starcoder-15b    | autohf   |             2 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|  6374 | Starcoder-15b    | autohf   |             4 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|  6419 | Starcoder-15b    | autohf   |             4 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|  6464 | Starcoder-15b    | autohf   |             4 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|  6914 | Starcoder-15b    | autohf   |             8 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|  6959 | Starcoder-15b    | autohf   |             8 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|  8772 | Starcoder2-3b    | autohf   |             1 |              256 |       280.349     |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|  8817 | Starcoder2-3b    | autohf   |             1 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|  8862 | Starcoder2-3b    | autohf   |             1 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|  9267 | Starcoder2-3b    | autohf   |             2 |              256 |       276.376     |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|  9312 | Starcoder2-3b    | autohf   |             2 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|  9357 | Starcoder2-3b    | autohf   |             2 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|  9807 | Starcoder2-3b    | autohf   |             4 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
|  9852 | Starcoder2-3b    | autohf   |             4 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 10302 | Starcoder2-3b    | autohf   |             8 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 10347 | Starcoder2-3b    | autohf   |             8 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 12554 | Starcoder2-7b    | autohf   |             1 |               64 |        21.9645    |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 12599 | Starcoder2-7b    | autohf   |             1 |              128 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 12644 | Starcoder2-7b    | autohf   |             1 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 12689 | Starcoder2-7b    | autohf   |             1 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 12734 | Starcoder2-7b    | autohf   |             1 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 13139 | Starcoder2-7b    | autohf   |             2 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 13184 | Starcoder2-7b    | autohf   |             2 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 13229 | Starcoder2-7b    | autohf   |             2 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 13634 | Starcoder2-7b    | autohf   |             4 |              256 |        16.0629    |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 13679 | Starcoder2-7b    | autohf   |             4 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 13724 | Starcoder2-7b    | autohf   |             4 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 14129 | Starcoder2-7b    | autohf   |             8 |              256 |        15.9823    |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 14174 | Starcoder2-7b    | autohf   |             8 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 14219 | Starcoder2-7b    | autohf   |             8 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 15624 | Bloom-1b7        | autohf   |             1 |              128 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 15669 | Bloom-1b7        | autohf   |             1 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 15714 | Bloom-1b7        | autohf   |             1 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 15759 | Bloom-1b7        | autohf   |             1 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 16119 | Bloom-1b7        | autohf   |             2 |              128 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 16164 | Bloom-1b7        | autohf   |             2 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 16209 | Bloom-1b7        | autohf   |             2 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 16254 | Bloom-1b7        | autohf   |             2 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 16614 | Bloom-1b7        | autohf   |             4 |              128 |        80.8206    |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 16659 | Bloom-1b7        | autohf   |             4 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 16704 | Bloom-1b7        | autohf   |             4 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 16749 | Bloom-1b7        | autohf   |             4 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 17109 | Bloom-1b7        | autohf   |             8 |              128 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 17154 | Bloom-1b7        | autohf   |             8 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 17199 | Bloom-1b7        | autohf   |             8 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 17244 | Bloom-1b7        | autohf   |             8 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 18967 | Bloom-3b         | autohf   |             1 |               64 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 19012 | Bloom-3b         | autohf   |             1 |              128 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 19057 | Bloom-3b         | autohf   |             1 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 19102 | Bloom-3b         | autohf   |             1 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 19147 | Bloom-3b         | autohf   |             1 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 19507 | Bloom-3b         | autohf   |             2 |              128 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 19552 | Bloom-3b         | autohf   |             2 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 19597 | Bloom-3b         | autohf   |             2 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 19642 | Bloom-3b         | autohf   |             2 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 20002 | Bloom-3b         | autohf   |             4 |              128 |        47.0253    |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 20047 | Bloom-3b         | autohf   |             4 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 20092 | Bloom-3b         | autohf   |             4 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 20137 | Bloom-3b         | autohf   |             4 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 20452 | Bloom-3b         | autohf   |             8 |               64 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 20497 | Bloom-3b         | autohf   |             8 |              128 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 20542 | Bloom-3b         | autohf   |             8 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 20587 | Bloom-3b         | autohf   |             8 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 20632 | Bloom-3b         | autohf   |             8 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 22749 | Bloom-7b1        | autohf   |             1 |               16 |        28.9328    |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 22794 | Bloom-7b1        | autohf   |             1 |               32 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 22839 | Bloom-7b1        | autohf   |             1 |               64 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 22884 | Bloom-7b1        | autohf   |             1 |              128 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 22929 | Bloom-7b1        | autohf   |             1 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 22974 | Bloom-7b1        | autohf   |             1 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 23019 | Bloom-7b1        | autohf   |             1 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 23334 | Bloom-7b1        | autohf   |             2 |               64 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 23379 | Bloom-7b1        | autohf   |             2 |              128 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 23424 | Bloom-7b1        | autohf   |             2 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 23469 | Bloom-7b1        | autohf   |             2 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 23514 | Bloom-7b1        | autohf   |             2 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 23874 | Bloom-7b1        | autohf   |             4 |              128 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 23919 | Bloom-7b1        | autohf   |             4 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 23964 | Bloom-7b1        | autohf   |             4 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 24009 | Bloom-7b1        | autohf   |             4 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 24369 | Bloom-7b1        | autohf   |             8 |              128 |        22.6383    |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 24414 | Bloom-7b1        | autohf   |             8 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 24459 | Bloom-7b1        | autohf   |             8 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 24504 | Bloom-7b1        | autohf   |             8 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 26576 | Codellama-13b-hf | autohf   |             1 |                8 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 26621 | Codellama-13b-hf | autohf   |             1 |               16 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 26666 | Codellama-13b-hf | autohf   |             1 |               32 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 26711 | Codellama-13b-hf | autohf   |             1 |               64 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 26756 | Codellama-13b-hf | autohf   |             1 |              128 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 26801 | Codellama-13b-hf | autohf   |             1 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 26846 | Codellama-13b-hf | autohf   |             1 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 26891 | Codellama-13b-hf | autohf   |             1 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 27161 | Codellama-13b-hf | autohf   |             2 |               32 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 27206 | Codellama-13b-hf | autohf   |             2 |               64 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 27251 | Codellama-13b-hf | autohf   |             2 |              128 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 27296 | Codellama-13b-hf | autohf   |             2 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 27341 | Codellama-13b-hf | autohf   |             2 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 27386 | Codellama-13b-hf | autohf   |             2 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 27701 | Codellama-13b-hf | autohf   |             4 |               64 |        11.7899    |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 27746 | Codellama-13b-hf | autohf   |             4 |              128 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 27791 | Codellama-13b-hf | autohf   |             4 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 27836 | Codellama-13b-hf | autohf   |             4 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 27881 | Codellama-13b-hf | autohf   |             4 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 28286 | Codellama-13b-hf | autohf   |             8 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 28331 | Codellama-13b-hf | autohf   |             8 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 28376 | Codellama-13b-hf | autohf   |             8 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 30538 | Codellama-34b-hf | autohf   |             1 |               32 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 30583 | Codellama-34b-hf | autohf   |             1 |               64 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 30628 | Codellama-34b-hf | autohf   |             1 |              128 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 30673 | Codellama-34b-hf | autohf   |             1 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 30718 | Codellama-34b-hf | autohf   |             1 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 30763 | Codellama-34b-hf | autohf   |             1 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 30808 | Codellama-34b-hf | autohf   |             2 |                1 |       nan         |          0.105297  | CUDA out of memory | ok                 |    nan        |
| 30853 | Codellama-34b-hf | autohf   |             2 |                2 |       nan         |          0.205505  | CUDA out of memory | ok                 |    nan        |
| 30898 | Codellama-34b-hf | autohf   |             2 |                4 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 30943 | Codellama-34b-hf | autohf   |             2 |                8 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 30988 | Codellama-34b-hf | autohf   |             2 |               16 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 31033 | Codellama-34b-hf | autohf   |             2 |               32 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 31078 | Codellama-34b-hf | autohf   |             2 |               64 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 31123 | Codellama-34b-hf | autohf   |             2 |              128 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 31168 | Codellama-34b-hf | autohf   |             2 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 31213 | Codellama-34b-hf | autohf   |             2 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 31258 | Codellama-34b-hf | autohf   |             2 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 31292 | Codellama-34b-hf | autohf   |             2 |                1 |       nan         |          0.105297  | CUDA out of memory | ok                 |    nan        |
| 31337 | Codellama-34b-hf | autohf   |             2 |                2 |       nan         |          0.205505  | CUDA out of memory | ok                 |    nan        |
| 31382 | Codellama-34b-hf | autohf   |             2 |                4 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 31427 | Codellama-34b-hf | autohf   |             2 |                8 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 31472 | Codellama-34b-hf | autohf   |             2 |               16 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 31517 | Codellama-34b-hf | autohf   |             2 |               32 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 31562 | Codellama-34b-hf | autohf   |             2 |               64 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 31607 | Codellama-34b-hf | autohf   |             2 |              128 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 31652 | Codellama-34b-hf | autohf   |             2 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 31697 | Codellama-34b-hf | autohf   |             2 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 31742 | Codellama-34b-hf | autohf   |             2 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 31877 | Codellama-34b-hf | autohf   |             4 |                4 |         5.3472    |        nan         | ok                 | CUDA out of memory |    nan        |
| 31922 | Codellama-34b-hf | autohf   |             4 |                8 |         5.33297   |        nan         | ok                 | CUDA out of memory |    nan        |
| 31967 | Codellama-34b-hf | autohf   |             4 |               16 |         5.18782   |        nan         | ok                 | CUDA out of memory |    nan        |
| 32012 | Codellama-34b-hf | autohf   |             4 |               32 |         5.62315   |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 32057 | Codellama-34b-hf | autohf   |             4 |               64 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 32102 | Codellama-34b-hf | autohf   |             4 |              128 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 32147 | Codellama-34b-hf | autohf   |             4 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 32192 | Codellama-34b-hf | autohf   |             4 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 32237 | Codellama-34b-hf | autohf   |             4 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 32597 | Codellama-34b-hf | autohf   |             8 |              128 |         4.21569   |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 32642 | Codellama-34b-hf | autohf   |             8 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 32687 | Codellama-34b-hf | autohf   |             8 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 32732 | Codellama-34b-hf | autohf   |             8 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 33286 | Codellama-70b-hf | autohf   |             4 |                8 |       nan         |          0.34832   | CUDA out of memory | ok                 |    nan        |
| 33309 | Codellama-70b-hf | autohf   |             4 |               16 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 33332 | Codellama-70b-hf | autohf   |             4 |               32 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 33355 | Codellama-70b-hf | autohf   |             4 |               64 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 33378 | Codellama-70b-hf | autohf   |             4 |              128 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 33401 | Codellama-70b-hf | autohf   |             4 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 33424 | Codellama-70b-hf | autohf   |             4 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 33447 | Codellama-70b-hf | autohf   |             4 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 33585 | Codellama-70b-hf | autohf   |             8 |               32 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 33608 | Codellama-70b-hf | autohf   |             8 |               64 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 33631 | Codellama-70b-hf | autohf   |             8 |              128 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 33654 | Codellama-70b-hf | autohf   |             8 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 33677 | Codellama-70b-hf | autohf   |             8 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 33700 | Codellama-70b-hf | autohf   |             8 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 34002 | Codellama-7b-hf  | autohf   |             1 |               16 |        23.5488    |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 34047 | Codellama-7b-hf  | autohf   |             1 |               32 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 34092 | Codellama-7b-hf  | autohf   |             1 |               64 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 34137 | Codellama-7b-hf  | autohf   |             1 |              128 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 34182 | Codellama-7b-hf  | autohf   |             1 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 34227 | Codellama-7b-hf  | autohf   |             1 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 34272 | Codellama-7b-hf  | autohf   |             1 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 34587 | Codellama-7b-hf  | autohf   |             2 |               64 |        22.9664    |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 34632 | Codellama-7b-hf  | autohf   |             2 |              128 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 34677 | Codellama-7b-hf  | autohf   |             2 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 34722 | Codellama-7b-hf  | autohf   |             2 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 34767 | Codellama-7b-hf  | autohf   |             2 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 35127 | Codellama-7b-hf  | autohf   |             4 |              128 |        20.2389    |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 35172 | Codellama-7b-hf  | autohf   |             4 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 35217 | Codellama-7b-hf  | autohf   |             4 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 35262 | Codellama-7b-hf  | autohf   |             4 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 35667 | Codellama-7b-hf  | autohf   |             8 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 35712 | Codellama-7b-hf  | autohf   |             8 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 35757 | Codellama-7b-hf  | autohf   |             8 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 37809 | Gemma-2b         | autohf   |             1 |               32 |        47.297     |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 37832 | Gemma-2b         | autohf   |             1 |               64 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 37855 | Gemma-2b         | autohf   |             1 |              128 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 37878 | Gemma-2b         | autohf   |             1 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 37901 | Gemma-2b         | autohf   |             1 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 37924 | Gemma-2b         | autohf   |             1 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 38085 | Gemma-2b         | autohf   |             2 |               64 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 38108 | Gemma-2b         | autohf   |             2 |              128 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 38131 | Gemma-2b         | autohf   |             2 |              256 |       nan         |        nan         | killed-noInfo      | CUDA out of memory |    nan        |
| 40623 | Gemma-7b         | autohf   |             1 |                8 |         7.22933   |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 40646 | Gemma-7b         | autohf   |             1 |               16 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 40669 | Gemma-7b         | autohf   |             1 |               32 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 40692 | Gemma-7b         | autohf   |             1 |               64 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 40715 | Gemma-7b         | autohf   |             1 |              128 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 40738 | Gemma-7b         | autohf   |             1 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 40761 | Gemma-7b         | autohf   |             1 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 40784 | Gemma-7b         | autohf   |             1 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 40899 | Gemma-7b         | autohf   |             2 |               16 |         1.96161   |        nan         | ok                 | CUDA out of memory |    nan        |
| 40922 | Gemma-7b         | autohf   |             2 |               32 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 40945 | Gemma-7b         | autohf   |             2 |               64 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 40968 | Gemma-7b         | autohf   |             2 |              128 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 40991 | Gemma-7b         | autohf   |             2 |              256 |       nan         |        nan         | killed-noInfo      | CUDA out of memory |    nan        |
| 45665 | Phi-1_5          | autohf   |             1 |              128 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 45710 | Phi-1_5          | autohf   |             1 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 45755 | Phi-1_5          | autohf   |             1 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 45800 | Phi-1_5          | autohf   |             1 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 46160 | Phi-1_5          | autohf   |             2 |              128 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 46205 | Phi-1_5          | autohf   |             2 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 46250 | Phi-1_5          | autohf   |             2 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 46295 | Phi-1_5          | autohf   |             2 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 46655 | Phi-1_5          | autohf   |             4 |              128 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 46700 | Phi-1_5          | autohf   |             4 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 46745 | Phi-1_5          | autohf   |             4 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 46790 | Phi-1_5          | autohf   |             4 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 47150 | Phi-1_5          | autohf   |             8 |              128 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 47195 | Phi-1_5          | autohf   |             8 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 47240 | Phi-1_5          | autohf   |             8 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 47285 | Phi-1_5          | autohf   |             8 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 49537 | Phi-2            | autohf   |             1 |              128 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 49582 | Phi-2            | autohf   |             1 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 49627 | Phi-2            | autohf   |             1 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 49672 | Phi-2            | autohf   |             1 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 50032 | Phi-2            | autohf   |             2 |              128 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 50077 | Phi-2            | autohf   |             2 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 50122 | Phi-2            | autohf   |             2 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 50167 | Phi-2            | autohf   |             2 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 50572 | Phi-2            | autohf   |             4 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 50617 | Phi-2            | autohf   |             4 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 50662 | Phi-2            | autohf   |             4 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 51067 | Phi-2            | autohf   |             8 |              256 |        35.8012    |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 51112 | Phi-2            | autohf   |             8 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 51157 | Phi-2            | autohf   |             8 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 53319 | Codestral-22b    | autohf   |             1 |               32 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 53364 | Codestral-22b    | autohf   |             1 |               64 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 53409 | Codestral-22b    | autohf   |             1 |              128 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 53454 | Codestral-22b    | autohf   |             1 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 53499 | Codestral-22b    | autohf   |             1 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 53544 | Codestral-22b    | autohf   |             1 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 53679 | Codestral-22b    | autohf   |             2 |                4 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 53724 | Codestral-22b    | autohf   |             2 |                8 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 53769 | Codestral-22b    | autohf   |             2 |               16 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 53814 | Codestral-22b    | autohf   |             2 |               32 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 53859 | Codestral-22b    | autohf   |             2 |               64 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 53904 | Codestral-22b    | autohf   |             2 |              128 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 53949 | Codestral-22b    | autohf   |             2 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 53994 | Codestral-22b    | autohf   |             2 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 54039 | Codestral-22b    | autohf   |             2 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 54399 | Codestral-22b    | autohf   |             4 |              128 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 54444 | Codestral-22b    | autohf   |             4 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 54489 | Codestral-22b    | autohf   |             4 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 54534 | Codestral-22b    | autohf   |             4 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 54939 | Codestral-22b    | autohf   |             8 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 54984 | Codestral-22b    | autohf   |             8 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 55029 | Codestral-22b    | autohf   |             8 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 55966 | Mistral-7b       | autohf   |             1 |               32 |        19.1098    |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 56008 | Mistral-7b       | autohf   |             1 |               64 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 56050 | Mistral-7b       | autohf   |             1 |              128 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 56092 | Mistral-7b       | autohf   |             1 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 56134 | Mistral-7b       | autohf   |             1 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 56176 | Mistral-7b       | autohf   |             1 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 56512 | Mistral-7b       | autohf   |             2 |              128 |        15.1274    |        nan         | CUDA out of memory | killed-noInfo      |    nan        |
| 57013 | Mistral-7b       | autohf   |             4 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 57055 | Mistral-7b       | autohf   |             4 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 57097 | Mistral-7b       | autohf   |             4 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 57475 | Mistral-7b       | autohf   |             8 |              256 |       nan         |        nan         | killed-noInfo      | CUDA out of memory |    nan        |
| 59684 | Mixtral-8x7b     | autohf   |             1 |               64 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 59729 | Mixtral-8x7b     | autohf   |             1 |              128 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 59774 | Mixtral-8x7b     | autohf   |             1 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 59819 | Mixtral-8x7b     | autohf   |             1 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 59864 | Mixtral-8x7b     | autohf   |             1 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 60134 | Mixtral-8x7b     | autohf   |             2 |               32 |       nan         |          1.73364   | CUDA out of memory | ok                 |    nan        |
| 60179 | Mixtral-8x7b     | autohf   |             2 |               64 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 60224 | Mixtral-8x7b     | autohf   |             2 |              128 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 60269 | Mixtral-8x7b     | autohf   |             2 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 60314 | Mixtral-8x7b     | autohf   |             2 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 60359 | Mixtral-8x7b     | autohf   |             2 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 60629 | Mixtral-8x7b     | autohf   |             4 |               32 |       nan         |          2.63479   | CUDA out of memory | ok                 |    nan        |
| 60674 | Mixtral-8x7b     | autohf   |             4 |               64 |       nan         |          4.10553   | CUDA out of memory | CUDA out of memory |    nan        |
| 60719 | Mixtral-8x7b     | autohf   |             4 |              128 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 60764 | Mixtral-8x7b     | autohf   |             4 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 60809 | Mixtral-8x7b     | autohf   |             4 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 60854 | Mixtral-8x7b     | autohf   |             4 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 61214 | Mixtral-8x7b     | autohf   |             8 |              128 |        10.146     |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 61259 | Mixtral-8x7b     | autohf   |             8 |              256 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 61304 | Mixtral-8x7b     | autohf   |             8 |              512 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |
| 61349 | Mixtral-8x7b     | autohf   |             8 |             1028 |       nan         |        nan         | CUDA out of memory | CUDA out of memory |    nan        |