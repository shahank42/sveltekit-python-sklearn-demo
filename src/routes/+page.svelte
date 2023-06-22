<script lang="ts">
    let val1: number;
    let val2: number;
    let prediction = "";

    const getXORPrediction = async () => {
        const res = await fetch("http://127.0.0.1:5000/xor", {
            method: "POST",
            body: JSON.stringify({
                val1: val1,
                val2: val2,
            }),
            headers: {
              "Content-type": "application/json; charset=UTF-8"
            }
        });
        const data = res.text();
        prediction = await data;
    }

</script>

<div>
    <form on:submit|preventDefault={getXORPrediction}>
        <label for="val1">Enter first value:</label>
        <input type="text" name="val1" bind:value={val1} />
        <br />

        <label for="val2">Enter second value:</label>
        <input type="text" name="val2" bind:value={val2} />
        <br />

        <button type="submit">Predict XOR!</button>
    </form>

    <span>XOR prediction is: {prediction}</span>
</div>