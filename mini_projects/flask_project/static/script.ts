const form = document.querySelector("#search-form") as HTMLFormElement;
const searchOutput = document.querySelector("#search-output") as HTMLDivElement;
const errorOutput = document.querySelector("#error-output") as HTMLDivElement;

form?.addEventListener("submit", async (e) => {
    e.preventDefault();
    const keywordInputElem = document.querySelector("#keywords") as HTMLInputElement;
    const keywords = keywordInputElem.value.trim().toLowerCase();

    const searchBaseUrl = "/search";
    const params = new URLSearchParams({
        q: keywords,
    });
    const searchApi = searchBaseUrl + "?" + params.toString();

    interface ITitleItem {
        id: number;
        title: string;
        year: number;
        type: string;
    }

    interface ISearchResult {
        results: ITitleItem[];
    }

    const res = await fetch(searchApi);
    const data: ISearchResult = await res.json();

    // Display data or error block
    if (data.results.length === 0) {
        errorOutput.style.display = "block";
        searchOutput.style.display = "none";
    } else {
        searchOutput.style.display = "block";
        errorOutput.style.display = "none";
    }

    const tableBody = document.querySelector("#search-table > tbody") as HTMLTableSectionElement;
    tableBody.replaceChildren();

    for (let titleItem of data.results) {
        const row = document.createElement("tr");

        const titleElem = document.createElement("td");
        titleElem.innerText = titleItem.title;

        const yearElem = document.createElement("td");
        yearElem.innerText = titleItem.year.toString();

        const typeElem = document.createElement("td");
        typeElem.innerText = titleItem.type;

        const url = "/streams/" + titleItem.id.toString();
        const streamLink = document.createElement("a");
        streamLink.setAttribute("href", url);
        streamLink.innerText = "Sources";

        const linkElm = document.createElement("td");
        linkElm.appendChild(streamLink);

        row.appendChild(titleElem);
        row.appendChild(yearElem);
        row.appendChild(typeElem);
        row.appendChild(linkElm);

        tableBody.appendChild(row);
    }

    const tableElem = document.querySelector("#search-table") as HTMLTableElement;
    tableElem.appendChild(tableBody);
});
