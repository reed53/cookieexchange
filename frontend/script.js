let voters = ['Ali', 'Andrew', 'Ariana', 'Bill', 'Bobby', 'Dhruv', 'Jack', 'Jordan', 'Kimy', 'Kwangmin',
    'Matt', 'Reed', 'Russel', 'Sai', 'Steven', 'Teddy'];

// common regex to replace in
const variableMatcherPattern = new RegExp('{([a-zA-Z0-9.]+)}', 'g');

function populatePage() {
  let voterSelect = document.getElementById("voterSelect");
  let voterTemplate = document.getElementById("voterTemplate").innerHTML;
  voterSelect.innerHTML = voters.map(voter => voterTemplate.replace(variableMatcherPattern,
    (match, text) => text === 'voter' ? voter : '')).join('<br>');


  let voteSelect = document.getElementById("voteSelect");
  let voteTemplate = document.getElementById("voteTemplate").innerHTML;
  voteSelect.innerHTML = voters.map(voter => voteTemplate.replace(variableMatcherPattern,
    (match, text) => text === 'voter' ? voter : '')).join('<br>');
}

function submitData() {
  let voter = document.querySelector('input[name="voter"]:checked').value;
  if (!voter) {
    alert('You need to select a voter');
  }

  let votes = [...document.querySelectorAll('input[name="vote"]:checked')].map(node => node.value);
  callLambda({votes, voter}, handleLambdaResponse);
}

function handleLambdaResponse(response) {
  if (response.error) {
    alert(response.error);
  } else {
    alert('Vote successfully submitted!');
  }
}

function callLambda(request, onCompletion) {
  const loader = document.getElementById('loader');
  loader.classList.add('is-active');
  const xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = () => {
    if (xhttp.readyState === 4) {
      let response;
      if (xhttp.status !== 200) {
        response = { error: `Error status ${xhttp.status} from lambda call` };
      } else {
        response = JSON.parse(xhttp.responseText);
      }
      loader.classList.remove('is-active');
      onCompletion(response);
    }
  };
  xhttp.open('POST', '/api/webapp', true);
  xhttp.send(JSON.stringify(request));
}