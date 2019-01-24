hs-chargemaster
===============

An exploration of procedure costs from published hospital chargemaster lists.

## About

The Centers for Medicare and Medicaid Services [released a new rule](https://www.cms.gov/newsroom/press-releases/cms-finalizes-changes-empower-patients-and-reduce-administrative-burden) to help improve access to hospital pricing.  Hospitals are now required to post their chargemaster lists on their websites in a machine-readable format.  We are looking to explore the opportunities with the aggregation, normalization, and distribution of these procedure price lists.

## Challenges and Risks

There are some possible challenges that have come up during the initial investigation.  This is a list of possible challenges and risks that will affect the outcome of this exploration.

- Not every hospital disclose the CPT code for us to match each one
- Hospitals may use different description (and with abbreviations), so it would be hard for us to equate each one between hospital
- Is average charge really something that is useful?  i.e. insurance-pay can be 6x or more than self-pay
- CMS may have more completed data we can use?

## Contributing

See [CONTRIBUTING](CONTRIBUTING.md) for additional information.

## Public domain

This project is in the worldwide [public domain](LICENSE.md). As stated in [CONTRIBUTING](CONTRIBUTING.md):

> This project is in the public domain within the United States, and copyright and related rights in the work worldwide are waived through the [CC0 1.0 Universal public domain dedication](https://creativecommons.org/publicdomain/zero/1.0/).
>
> All contributions to this project will be released under the CC0 dedication. By submitting a pull request, you are agreeing to comply with this waiver of copyright interest.
