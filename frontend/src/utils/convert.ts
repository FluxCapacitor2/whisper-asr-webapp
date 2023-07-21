import type { WhisperResult } from "../types/WhisperResult";

function formatTimestamp(
  seconds: number,
  alwaysIncludeHours = false,
  decimalMarker = ".",
) {
  let milliseconds = Math.round(seconds * 1000.0);

  let hours = Math.floor(milliseconds / 3_600_000);
  milliseconds -= hours * 3_600_000;

  let minutes = Math.floor(milliseconds / 60_000);
  milliseconds -= minutes * 60_000;

  seconds = Math.floor(milliseconds / 1_000);
  milliseconds -= seconds * 1_000;

  let hoursMarker =
    alwaysIncludeHours || hours > 0
      ? hours.toString().padStart(2, "0") + ":"
      : "";

  return `${hoursMarker}${minutes.toString().padStart(2, "0")}:${seconds
    .toString()
    .padStart(2, "0")}${decimalMarker}${milliseconds
    .toString()
    .padStart(3, "0")}`;
}

export function getContent(
  result: WhisperResult,
  format: "txt" | "vtt" | "srt" | "tsv" | "json",
) {
  switch (format) {
    case "txt": {
      return result.segments.map((segment) => segment.text.trim()).join("\n");
    }
    case "vtt": {
      return (
        "WEBVTT\n\n" +
        result.segments
          .map((segment) => {
            return `${formatTimestamp(segment.start)} --> ${formatTimestamp(
              segment.end,
            )}\n${segment.text.trim().replace("-->", "->")}\n`;
          })
          .join("\n")
      );
    }
    case "srt": {
      return result.segments
        .map(
          (segment, i) =>
            `${i + 1}\n${formatTimestamp(
              segment.start,
              true,
              ",",
            )} --> ${formatTimestamp(segment.end, true, ",")}\n${segment.text
              .trim()
              .replace("-->", "->")}\n`,
        )
        .join("\n");
    }
    case "tsv": {
      return (
        "start\tend\ttext\n" +
        result.segments
          .map((segment) => {
            return `${Math.round(1000 * segment.start)}\t${Math.round(
              1000 * segment.end,
            )}\t${segment.text.trim().replace("\t", " ")}`;
          })
          .join("\n")
      );
    }
    case "json": {
      return JSON.stringify(result);
    }
  }
}
