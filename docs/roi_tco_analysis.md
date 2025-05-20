# ROI and TCO Analysis

## Total Cost of Ownership (TCO)
- **Infrastructure Costs:** $1,200/month for AWS compute (EC2, S3, Lambda)
- **Development & Maintenance:** 2 FTEs @ $10,000/month = $20,000/month
- **Licensing & Tools:** $1,500/month (MLflow, monitoring, vector DB)

**Monthly TCO:** $22,700

## Return on Investment (ROI)
Assume an agricultural client with:
- **Annual crop yield:** 100,000 kg
- **Revenue per kg:** $5
- **Current loss rate:** 10% (10,000 kg) due to disease & mismanagement
- **Post-deployment loss rate:** 5% (5,000 kg)

**Annual saved yield:** 5,000 kg × $5 = $25,000  
**Additional revenue:** $25,000/year

**ROI Calculation:**  
ROI = (Annual Gain - Annual TCO) / Annual TCO  
Annual TCO = $22,700 × 12 = $272,400  
ROI = ($25,000 - $272,400) / $272,400 ≈ -0.08 (negative in first year)

**Payback Period:**  
At break-even, need yield improvement or cost reduction improvements.

## Sensitivity Analysis
- **If infrastructure optimized** to $800/month, TCO drops to $20,000/month, ROI improves.
- **Scaling to 1M kg yield** reduces TCO per kg, significantly improving ROI.
