

function createTable(start, end) {
	//  compute dividing points between small, medium and large
	let valList = [];
	for(let r = start; r <= end; r++ ) {
		for(let c = start; c <= end; c++ ) {
			valList.push(r*c);
		}
	}
	valList.sort(function(a,b){return a-b;});  // in ruby <=>
	let val1 = valList[Math.floor(valList.length/3)];
	let val2 = valList[Math.floor(2*valList.length/3)];
	valList = null;
	//alert(val1);
	//alert(val2);

	// create table node
	let table = document.createElement("table");
	// find the div node in the page which will contain the table.
	let tabDiv = document.getElementById("table");
	// clean up any table already created.
	let last = tabDiv.lastChild;
	while(last) {
		tabDiv.removeChild(last);
		last = tabDiv.lastChild;
	}
	// attach the table to the div node.
	tabDiv.appendChild(table);
	// create header row
	let row = document.createElement("tr");
	table.appendChild(row);
	let cell = document.createElement("th");
	row.appendChild(cell);
	for(let col = start; col <= end; col++ ) {
		cell = document.createElement("th");
		row.appendChild(cell);
		let txt = document.createTextNode("" + col);
		cell.appendChild(txt);

	}
	for(let r = start; r <= end; r++ ) {
		// create body row
			// creating row
			row = document.createElement("tr");
			table.appendChild(row);
			// putting a row header
			cell = document.createElement("th");
			row.appendChild(cell);
			let txt = document.createTextNode(r + "" );
			cell.appendChild(txt);
			for(let col = start; col <= end; col++ ) {
				let value = r*col;
				cell = document.createElement("td");
				row.appendChild(cell);
				txt = document.createTextNode("" + (value));
				cell.appendChild(txt);
				// check if cell is large, medium or small
				if(value < val1) {
					// set class to .val0
					cell.setAttribute("class", "val0");
				} else if(value < val2) {
					// set class to .val1
					cell.setAttribute("class", "val1");
				} else {
					// set class to .val2
					cell.setAttribute("class", "val2");
				}

			}
	}
}

function doScript() {
	let start_value = document.getElementById("start-value").value;
	let end_value = document.getElementById("end-value").value;
	//alert(start_value + " --> " + end_value);
	createTable(+start_value, +end_value);
	//return false;
}


window.addEventListener("load",
	function (){
		let goButton = document.getElementById("go-button");
		goButton.addEventListener('click', doScript);
	});

