import { saveAs } from "file-saver";

export function fileSize(fileSize: number) {
  if (fileSize < 1000) {
    return `${fileSize} bytes`;
  } else if (fileSize < 1_000_000) {
    return `${Math.round(fileSize / 1_000)} kB`;
  } else if (fileSize < 1_000_000_000) {
    return `${Math.round(fileSize / 1_000_000)} MB`;
  } else {
    return `${Math.round(fileSize / 1_000_000_000)} GB`;
  }
}

export async function fetchModels() {
  const res = await fetch("http://localhost:8000/models");
  return await res.json();
}

export function download(filename, content) {
  const blob = new Blob([content], { type: "text/plain;charset=utf-8" });
  saveAs(blob, filename);
}
