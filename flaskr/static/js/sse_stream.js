var stream_tag = document.getElementById('stream')
var stream_name = stream_tag.getAttribute("data-stream-name")

var template = {'<>':'tr','html':[
                    {'<>':'td','text':'${job_name}'},
                    {'<>':'td','text':'${job_state}'}
                ]};

var targetContainer = document.getElementById("target_body");

var eventSource = new EventSource("streams/"+stream_name)
  eventSource.onmessage = function(e) {
  //for debugging:
  //console.log(e.data);
  targetContainer.innerHTML = json2html.transform(e.data,template);
};
