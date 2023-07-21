<script lang="ts">
  export let language: string;
  export let english: boolean;

  $: if (english) {
    language = "english";
  }

  // Whisper's list of supported languages with a <50% word error rate
  // see https://platform.openai.com/docs/guides/speech-to-text/supported-languages
  const languages = [
    "Afrikaans",
    "Arabic",
    "Armenian",
    "Azerbaijani",
    "Belarusian",
    "Bosnian",
    "Bulgarian",
    "Catalan",
    "Chinese",
    "Croatian",
    "Czech",
    "Danish",
    "Dutch",
    "English",
    "Estonian",
    "Finnish",
    "French",
    "Galician",
    "German",
    "Greek",
    "Hebrew",
    "Hindi",
    "Hungarian",
    "Icelandic",
    "Indonesian",
    "Italian",
    "Japanese",
    "Kannada",
    "Kazakh",
    "Korean",
    "Latvian",
    "Lithuanian",
    "Macedonian",
    "Malay",
    "Marathi",
    "Maori",
    "Nepali",
    "Norwegian",
    "Persian",
    "Polish",
    "Portuguese",
    "Romanian",
    "Russian",
    "Serbian",
    "Slovak",
    "Slovenian",
    "Spanish",
    "Swahili",
    "Swedish",
    "Tagalog",
    "Tamil",
    "Thai",
    "Turkish",
    "Ukrainian",
    "Urdu",
    "Vietnamese",
    "Welsh",
  ];
</script>

<select
  name="language"
  bind:value={language}
  class="dark:bg-gray-700 dark:text-white disabled:text-gray-400"
  disabled={english}
>
  <option value="">Auto-detect</option>
  {#each languages as name}
    <option value={name.toLowerCase()}>{name}</option>
  {/each}
</select>
