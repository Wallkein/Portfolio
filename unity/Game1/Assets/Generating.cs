using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Generating : MonoBehaviour
{
    public GameObject road;
    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Create()
    {
        GameObject roadClone = Instantiate(road, new Vector3(62, 1, -75), Quaternion.identity);
        Destroy(roadClone, 30f);
    }
    void OnTriggerEnter(Collider col)
    {
        if (col.gameObject.tag == "Player")
        {
            Create();
        }
    }
}