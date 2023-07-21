<script lang="ts">
  import ModelSelectOption from "./ModelSelectOption.svelte";
  import Tooltip from "./Tooltip.svelte";
  import Bugs from "./icons/Bugs.svelte";
  import CircleQuestion from "./icons/CircleQuestion.svelte";
  import Frog from "./icons/Frog.svelte";
  import Hippo from "./icons/Hippo.svelte";
  import Otter from "./icons/Otter.svelte";
  import Seedling from "./icons/Seedling.svelte";

  export let model: string;
  export let models: Promise<{ [key: string]: boolean }>;
</script>

<fieldset>
  <legend class="text-xs uppercase font-bold mb-2">
    Choose a model
    <Tooltip
      tip={`"Tiny" is the fastest and has the lowest download size, but it's the least accurate. "Base" is the default. "Large" is the slowest and has the highest download size, but it's the most accurate.`}
    >
      <CircleQuestion
        class="fill-gray-400 dark:fill-gray-500 w-4 h-4 -mb-0.5"
      />
    </Tooltip>
  </legend>
  <div class="grid grid-cols-5 gap-2 justify-around">
    <ModelSelectOption id="tiny" name="Tiny" bind:model {models}>
      <Bugs />
    </ModelSelectOption>

    <ModelSelectOption id="base" name="Base" bind:model {models}>
      <Frog />
    </ModelSelectOption>

    <ModelSelectOption id="small" name="Small" bind:model {models}>
      <Seedling />
    </ModelSelectOption>

    <ModelSelectOption id="medium" name="Medium" bind:model {models}>
      <Otter />
    </ModelSelectOption>

    <ModelSelectOption id="large" name="Large" bind:model {models}>
      <Hippo />
    </ModelSelectOption>
  </div>
</fieldset>

<fieldset>
  <legend class="text-xs uppercase font-bold mb-2">
    English-only models
    <Tooltip
      tip="English-only models tend to perform better on English tasks, especially on the Tiny and Base models."
    >
      <CircleQuestion
        class="fill-gray-400 dark:fill-gray-500 w-4 h-4 -mb-0.5"
      />
    </Tooltip>
  </legend>
  <div class="grid grid-cols-5 gap-2 justify-around">
    <ModelSelectOption id="tiny.en" name="Tiny" bind:model {models} />
    <ModelSelectOption id="base.en" name="Base" bind:model {models} />
    <ModelSelectOption id="small.en" name="Small" bind:model {models} />
    <ModelSelectOption id="medium.en" name="Medium" bind:model {models} />
  </div>
</fieldset>
