# medi_price
Application to predict medical procedure cost

## Data Structure

### Raw Data
 ref: https://data.cms.gov/Medicare-Inpatient/Inpatient-Prospective-Payment-System-IPPS-Provider/97k6-zzx3

1. DRG Definition
    definition: Code and description identifying the DRG. DRGs are a classification system that groups similar clinical conditions (diagnoses) and the procedures furnished by the hospital during the stay.

2. Provider Id
    definition: Provider Identifier billing for inpatient hospital services.

3. Provider Name
    definition: Name of the provider.

4. Provider Street Address
    definition: Street address in which the provider is physically located.

5. Provider City
    definition: City in which the provider is physically located.

6. Provider State
    definition: State in which the provider is physically located.

7. Provider Zip Code
    definition: Zip code in which the provider is physically located.

8. Hospital Referral Region Description
    definition: HRR in which the provider is physically located.

9. Total Discharges
    definition: The number of discharges billed by the provider for inpatient hospital services.

10. Average Covered Charges
    definition: The provider's average charge for services covered by Medicare for all discharges in the DRG. These will vary from hospital to hospital because of differences in hospital charge structures.

11. Average Total Payments
    definition: The average of Medicare payments to the provider for the DRG including the DRG amount, teaching,  disproportionate share, capital, and outlier payments for all cases. Also included are co-payment and deductible amounts that the patient is responsible for

12. Average Medicare Payments


## Model:
    Currently we are using the columns 1. DRG Definition and 6. Provider State as features to predict 11. Average Total Payments

