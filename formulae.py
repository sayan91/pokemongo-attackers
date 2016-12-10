=IF(NR=100,CEILING(AD6/V6,1),AD6/V6)*(R6*(1+T6*0.25))+Y6*(1+AA6*0.25)*(1+($AM$1*AB6/100))






=
  FLOOR(
    100000/Average Weave Cycle Length (ms),1
    )
  *
  (
    PWR_CHARGE
    *
    (1+CHARGE_STAB*0.25)
    *
    (1+(Crit Damage Bonus*Crit%/100))
  )
  +
  CEILING(FLOOR(100000/Average Weave Cycle Length (ms),1) * IF(NRG_CHARGE=100,CEILING(NRG_CHARGE/NRG_BASIC,1),NRG_CHARGE/NRG_BASIC),1) * (PWR_BASIC*(1+(STAB_BASIC*0.25)))+FLOOR((100000-(FLOOR(100000/Average Weave Cycle Length (ms),1) * (SPD_CHARGE+Charge Delay (ms)) + CEILING(FLOOR(100000/Average Weave Cycle Length (ms),1) * IF(NRG_CHARGE=100,CEILING(NRG_CHARGE/NRG_BASIC,1),NRG_CHARGE/NRG_BASIC),1)*SPD_BASIC))/SPD_BASIC,1)*(PWR_BASIC*(1+(STAB_BASIC*0.25)))
