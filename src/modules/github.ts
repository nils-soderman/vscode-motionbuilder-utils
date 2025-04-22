import * as logging from "./logging";
import * as utils from "./utils";


const GITHUB_API_URL = "https://api.github.com/repos";
const GITHUB_API_HEADERS = {
    'User-Agent': 'VSCode-MotionBuilder-Extension'  // eslint-disable-line @typescript-eslint/naming-convention
};


/* eslint-disable @typescript-eslint/naming-convention */
interface IContent {
    name: string;
    path: string;
    sha: string;
    size: number;
    url: string;
    git_url: string;
    download_url: string;
    type: string;
    _links: {
        self: string;
        git: string;
        html: string;
    };
}
/* eslint-enable @typescript-eslint/naming-convention */


/**
 * Parse the data from the GitHub API into an array of IGitHubApiContent objects.
 */
function parseGitHubApiContent(data: string): Array<IContent> {
    try {
        return JSON.parse(data) as Array<IContent>;
    }
    catch (error) {
        logging.log(data);
        logging.showErrorMessage("Failed to parse available versions", error as Error);
        throw error;
    }
}


export function getRequest(url: string, timeout = 10_000): Promise<string> {
    return utils.httpsGetRequest(url, { timeout, headers: GITHUB_API_HEADERS });
}



export async function getContents(repository: string, path: string, timeout = 10_000): Promise<Array<IContent>> {
    const url = `${GITHUB_API_URL}/${repository}/contents/${path}`;

    let data: string;

    try {
        data = await getRequest(url, timeout);
    }
    catch (error) {
        logging.showErrorMessage("Failed to fetch available versions", error as Error);
        throw error;
    }

    return parseGitHubApiContent(data);
}