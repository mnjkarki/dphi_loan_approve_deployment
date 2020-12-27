function getRadioTypeValue(name) {
  var radioEle = document.getElementsByName(name);
  for (var i in radioEle) {
    if (radioEle[i].checked) {
      return parseInt(radioEle[i].value);
    }
  }
  return -1; // Invalid Value
}

function getValue(name){
  return document.getElementsByName(name)[0].value
}

function onClickedLoanEligible(event) {
  var genderVal = getRadioTypeValue('gender');
  var marriedVal = getRadioTypeValue('married');
  var selfEmpVal = getRadioTypeValue('selfEmployed');
  var educationVal = getRadioTypeValue('education');

  var applicantIncomeVal = getValue('applicant_income');
  var coApplicantIncomeVal = getValue('coapplicant_income');
  var loanAmountVal = getValue('loan_amount');
  var loanAmountTermVal = getValue('loan_amount_term');
  var creditHistoryVal = getValue('credit_history');

  var dependents = getValue('dependents');
  var propertyArea = getValue('property_area');
  //console.log("Estimate price button clicked"+ );


  var loanStatusEle = document.getElementById("uiLoanApproveInfo");
  var url = "/predict_loan_approve"; 

  $.post(
    url,
    {
      gender: genderVal,
      married: marriedVal,
      selfEmployed: selfEmpVal,
      education: educationVal,
      applicant_income: parseInt(applicantIncomeVal),
      coapplicant_income: parseFloat(coApplicantIncomeVal),
      loan_amount: parseFloat(loanAmountVal),
      loan_amount_term: parseFloat(loanAmountTermVal),
      credit_history: parseFloat(creditHistoryVal),
      dependents: dependents,
      propArea: propertyArea
    },
    function (data, status) {
      console.log(data.loan_status);
      loanStatusEle.innerHTML =
        "<h2>" + (data.loan_status == 1 ? "congrats, your loan is approved" : "sorry your loan is not approved")+"</h2>";
      console.log(status);
    }
  );
}

function onPageLoad() {
  console.log("document loaded");

}

window.onload = onPageLoad;